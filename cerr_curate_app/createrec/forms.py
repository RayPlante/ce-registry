"""
a module defining Form subclasses used in the createrec page/app
"""
import pdb
import os
from collections import OrderedDict
from collections.abc import Mapping

from django import forms as djforms
from django.utils.html import conditional_escape
from django.forms.utils import ErrorDict

from cerr_curate_app.forms import MultiForm, CerrErrorList

app_name = 'createrec'

class CreateWidget(djforms.widgets.MultiWidget):
    template_name = os.path.join(app_name, 'create.html')

    def __init__(self, attrs=None):
        self.name = djforms.TextInput()
        self.homepage = djforms.TextInput()
        components = OrderedDict([
            ('name',     self.name),
            ('homepage', self.homepage)
        ])
        super(CreateWidget, self).__init__(components, attrs)

    def decompress(self, value):
        if value is None:
            value = {}
        if not isinstance(value, Mapping):
            raise TypeError("CreateWidget: value to decompress is not a dict: "+str(type(value)))
        return [value.get('name'), value.get('homepage')]

    def get_context(self, name, value, attrs):
        """
        return the context that will be passed to the widget template
        """
        context = super().get_context(name, value, attrs)
        subwidgets = context['widget']['subwidgets']
        context['widget']['subwidgets'] = {
            'name': subwidgets[0],
            'homepage': subwidgets[1]
        }
        return context
        

class CreateField(djforms.fields.MultiValueField):
    """
    A Field for collecting inputs for creating a new record

    It includes:
     * a text field for entering a mnemonic name
     * a URL field for entering the resource's landing page
     * an array of radio buttons for selecting a type
    """
    widget = CreateWidget

    def __init__(self, **kw):
        self.name = djforms.CharField(required=True)
        self.homepage = djforms.URLField()

        super(CreateField, self).__init__([self.name, self.homepage], label='', **kw)
                                          

    def compress(self, values):
        out = {}
        out['name'] = self.name.clean(values[0])
        out['homepage'] = self.name.clean(values[1])
        return out
            
    

class CreateForm(djforms.Form):
    """
    A Form for creating an initial draft of a record.

    It includes:
     * a text field for entering a mnemonic name
     * a URL field for entering the resource's landing page
     * an array of radio buttons for selecting a type
    """
    template_name = 'createrec/create.html'
    name = djforms.CharField(required=True)
    homepage = djforms.URLField(required=False)

    def __init__(self, data=None, files=None, is_top=True, show_errors=None, **kwargs):
        self.is_top = is_top
        self.show_aggregate_errors = show_errors
        self.disabled = False
        if self.show_aggregate_errors is None:
            self.show_aggregate_errors = self.is_top
        if 'error_class' not in kwargs:
            kwargs['error_class'] = CerrErrorList
        super(CreateForm, self).__init__(data, files, **kwargs)
        
    @property
    def name_errors(self):
        """
        return the errors associated with the name input
        """
        return self.errors.get("name", self.error_class(error_class="errorlist", renderer=self.renderer))
        
    @property
    def homepage_errors(self):
        """
        return the errors associated with the homepage input
        """
        return self.errors.get("homepage", self.error_class(error_class="errorlist", renderer=self.renderer))

    def full_clean(self):
        if self.disabled:
            self._errors = ErrorDict()
            self.cleaned_data = {}
        else:
            super(CreateForm, self).full_clean()

class MethodSelect(djforms.RadioSelect):
    option_template_name = 'createrec/method_option.html'

class StartForm(MultiForm):
    """
    Form that allows a user to edit a new record
    """

    template_name = 'createrec/start.html'
    xmlfile = djforms.FileField(widget=djforms.FileInput(attrs={'class': 'form-control'}), required=False)
    start_meth = djforms.ChoiceField(widget=MethodSelect, required=True, choices=[
        ('create', 'Create a new record from scratch'),
        ('upload', 'Upload an existing XML document')
    ])

    def __init__(self, data=None, files=None, is_top=True, show_errors=None, **kwargs):
        self.create = CreateForm(data, files, is_top=False)
        if 'error_class' not in kwargs:
            kwargs['error_class'] = CerrErrorList
        super(StartForm, self).__init__(data, files, {'create': self.create},
                                        is_top, show_errors, **kwargs)
        
    def _clean_form(self):
        if self.cleaned_data.get('start_meth') == 'upload':
            self.create.disabled = True
            if not self.files.get('xmlfile'):
                if 'xmlfile' not in self._errors:
                    self._errors['xmlfile'] = CerrErrorList([], error_class="errorlist",
                                                            renderer=self.renderer)
                self._errors['xmlfile'].append('Please select an XML file to upload')
        super(StartForm, self)._clean_form()


