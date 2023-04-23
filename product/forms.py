from django import forms
from .models import Product
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CreateProductForm(forms.Form):
    title = forms.CharField(required=True, max_length=255, widget=forms.TextInput(attrs={"placeholder": "Product name"}))
    desc = forms.CharField(required=False,
                           widget=forms.Textarea(attrs={
                               "class": "",
                               "id": "productDesc",
                               "rows": 20,
                               "cols": 50,
                           }))
    price = forms.DecimalField(max_digits=12, decimal_places=2)

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError(_("Price must be greater than 0"))

        return price
