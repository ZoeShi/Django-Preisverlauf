from django import forms
from polls.models import Product_id


class UploadFileForm(forms.Form):
    file = forms.FileField()


class Product_idForm(forms.ModelForm):
    class Meta:
        model = Product_id,
        fields = ['Product', 'GuenstigsterPreis']
