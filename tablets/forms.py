from django import forms
from . import models

class CreateTablet(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-group',
            'placeholder': 'Enter a name',
        }
    ))
    storage_size = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-group',
            'placeholder': 'Enter a value',
            'type':'number',
        }
    ))
    release_year = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-group',
            'placeholder': 'Enter a year',
            'type':'number',
        }
    ))
    
    class Meta:
        model = models.Tablet
        fields = ['name', 'description', 'brand', 'storage_size', 'release_year', 'picture']

class CreateBrand(forms.ModelForm):
    
    class Meta:
        model = models.Brand
        fields = ['name', 'founder', 'country', 'logo']