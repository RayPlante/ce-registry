from django import forms
from django.db import models
from core_main_registry_app.utils.fancytree.widget import FancyTreeWidget





class NameForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    address = forms.CharField(label='address', max_length=100)
    number = forms.IntegerField(label='number')
    country = forms.CharField(label='country', max_length=100)





