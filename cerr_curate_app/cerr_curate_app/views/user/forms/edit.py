"""
a module defining Forms used to edit an existing draft record
"""
import os
from collections import OrderedDict
from collections.abc import Mapping

from django import forms as forms
from django.utils.html import conditional_escape
from django.forms.utils import ErrorDict

from .base import MultiForm, CerrErrorList

__all__ = ['EditForm']

TMPL8S = 'cerr_curate_app/user/forms/'

class EditForm(MultiForm):
    """
    Form that allows a user to create a new record.  

    The cleaned_data provides data collected from the form in the following fields:
    :param str homepage:   the resource's home page URL
    """
    template_name = TMPL8S + 'editform.html'
    homepage = forms.URLField(required=True)

    def __init__(self, data=None, is_top=True, show_errors=None, **kwargs):
        self.is_top = is_top
        self.show_aggregate_errors = show_errors
        if self.show_aggregate_errors is None:
            self.show_aggregate_errors = self.is_top
        if 'error_class' not in kwargs:
            kwargs['error_class'] = CerrErrorList
        super(EditForm, self).__init__(data, **kwargs)
