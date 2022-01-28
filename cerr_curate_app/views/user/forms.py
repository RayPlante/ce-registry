from django import forms
from django.db import models
from core_main_registry_app.utils.fancytree.widget import FancyTreeWidget
from core_main_registry_app.components.category.models import Category

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title





class NameForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    address = forms.CharField(label='address', max_length=100)
    number = forms.IntegerField(label='number')
    country = forms.CharField(label='country', max_length=100)





