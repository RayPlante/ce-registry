"""
a module defining Forms used to edit an existing draft record
"""
import os
from collections import OrderedDict
from collections.abc import Mapping

from django import forms as forms
from django.utils.html import conditional_escape
from django.forms.utils import ErrorDict
from cerr_curate_app.utils.fancytree.widget import FancyTreeWidget
from .base import MultiForm, CerrErrorList, ComposableForm

__all__ = ['EditForm']

TMPL8S = 'cerr_curate_app/user/forms/'
from .selectrestype import ResourceTypeChoiceField


class ProductForm(ComposableForm):
    choices = ("batteries", "electronics ", "packaging","textiles"),
    template_name = TMPL8S + 'ProductForm.html'
    restype = forms.MultipleChoiceField(choices = choices,widget = forms.RadioSelect)
    def __init__(self, data=None, files=None, is_top=True, show_errors=None, **kwargs):
        self.is_top = is_top
        self.show_aggregate_errors = show_errors
        self.disabled = False
        if self.show_aggregate_errors is None:
            self.show_aggregate_errors = self.is_top
        if 'error_class' not in kwargs:
            kwargs['error_class'] = CerrErrorList
        super(ProductForm, self).__init__(data,files,**kwargs)

    @property
    def homepage_errors(self):
        """
        return the errors associated with the homepage input
        """
        return self.errors.get("homepage", self.error_class(error_class="errorlist"))


    def full_clean(self):
        if self.disabled:
            self._errors = ErrorDict()
            self.cleaned_data = {}
        else:
            super(ProductForm, self).full_clean()

class UrlForm(ComposableForm):
    template_name = TMPL8S + 'urlform.html'
    homepage = forms.URLField(label='Home Page URL')

    def __init__(self, data=None, files=None, is_top=True, show_errors=None, **kwargs):
        self.is_top = is_top
        self.show_aggregate_errors = show_errors
        self.disabled = False
        if self.show_aggregate_errors is None:
            self.show_aggregate_errors = self.is_top
        if 'error_class' not in kwargs:
            kwargs['error_class'] = CerrErrorList
        super(UrlForm, self).__init__(data,files,**kwargs)

    @property
    def homepage_errors(self):
        """
        return the errors associated with the homepage input
        """
        return self.errors.get("homepage", self.error_class(error_class="errorlist"))


    def full_clean(self):
        if self.disabled:
            self._errors = ErrorDict()
            self.cleaned_data = {}
        else:
            super(UrlForm, self).full_clean()


class CreateForm(ComposableForm):
    """
    A Form for creating an initial draft of a record.

    It includes:
     * a text field for entering a mnemonic name
     * a URL field for entering the resource's landing page
     * an array of radio buttons for selecting a type
    """
    template_name = TMPL8S + 'createform.html'
    name = forms.CharField(required=True)
    homepage = forms.URLField(required=False)
    restype = ResourceTypeChoiceField()

    def __init__(self, data=None,  is_top=True, show_errors=None, **kwargs):
        self.is_top = is_top
        self.show_aggregate_errors = show_errors
        self.disabled = False
        if self.show_aggregate_errors is None:
            self.show_aggregate_errors = self.is_top
        if 'error_class' not in kwargs:
            kwargs['error_class'] = CerrErrorList
        super(CreateForm, self).__init__(data,  **kwargs)

    @property
    def name_errors(self):
        """
        return the errors associated with the name input
        """
        return self.errors.get("name", self.error_class(error_class="errorlist"))

    @property
    def homepage_errors(self):
        """
        return the errors associated with the homepage input
        """
        return self.errors.get("homepage", self.error_class(error_class="errorlist"))

    @property
    def restype_errors(self):
        """
        return the errors associated with the homepage input
        """
        return self.errors.get("restype", self.error_class(error_class="errorlist"))

    def full_clean(self):
        if self.disabled:
            self._errors = ErrorDict()
            self.cleaned_data = {}
        else:
            super(CreateForm, self).full_clean()


class EditForm(MultiForm):
    """
    Form that allows a user to create a new record.  

    The cleaned_data provides data collected from the form in the following fields:
    :param str homepage:   the resource's home page URL
    """
    template_name = TMPL8S + 'editform.html'
    title = forms.CharField(label ='Title of Resource Type' ,required=True)
    description = forms.CharField(widget=forms.Textarea, label='Description')

    def __init__(self,data=None,files=None, title=None, is_top=True, show_errors=None, **kwargs):
        if data.get('homepage') :
            self.urlform = UrlForm(data,files,is_top=False,initial = {'homepage': data['homepage']})
        else :
            self.urlform = UrlForm(data, files, is_top=False)
        self.productform = ProductForm(data, files, is_top = False)
        self.material = MaterialTypeForm()
        self.is_top = is_top
        self.show_aggregate_errors = show_errors
        self.title = title
        if self.show_aggregate_errors is None:
            self.show_aggregate_errors = self.is_top
        if 'error_class' not in kwargs:
            kwargs['error_class'] = CerrErrorList
        super(EditForm, self).__init__(data,{'urlform':self.urlform, 'productform':self.productform},**kwargs)

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Fruit(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

class MaterialTypeForm(forms.Form):
    fields = ('name', 'categories')
    categories = Fruit.objects.order_by('tree_id', 'lft')
    widgets = forms.ModelMultipleChoiceField(
       queryset=categories,
       widget=FancyTreeWidget(queryset=categories, count_mode=True)
    )