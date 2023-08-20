from django import forms

from django.db import models
from django.forms import ModelForm, Textarea, TextInput, NumberInput, CheckboxInput, FileInput

class AdvertisementForms(forms.Form):
    title =         forms.CharField( max_length=60, widget=forms.TextInput(attrs={'class': 'from-control-lg'}))
    description =   forms.CharField( widget= forms.Textarea(attrs={'class': 'from-control-lg'}))
    price =         forms.DecimalField( widget=forms.NumberInput(attrs={'class': 'from-control-lg'}))
    is_auction =    forms.BooleanField( required=True, widget=forms.CheckboxInput(attrs={'class': 'from-control-lg'}))
    image =         forms.ImageField(widget=forms.FileInput(attrs={'class': 'from-control-lg'}))