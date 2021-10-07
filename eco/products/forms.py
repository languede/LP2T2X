from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'image',
            'description',
            'price',
            'is_eco'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField()
    image = forms.ImageField()
    description = forms.CharField()
    price = forms.DecimalField()
    ecological = forms.BooleanField(required=False)
