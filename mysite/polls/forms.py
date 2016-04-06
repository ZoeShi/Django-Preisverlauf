from django import forms
from .models import Product
from .admin import *


class UploadFileForm(forms.Form):
    file = forms.FileField()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Product', 'GuenstigsterPreis']



class Auswahlbox(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Kategorie']





'''class Button(forms.ModelForm):
    class Meta:
        if Button :'''





