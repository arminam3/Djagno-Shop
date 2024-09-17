from django import forms

class AddProductToCartForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
    replace_quantity = forms.BooleanField(required=False, widget=forms.HiddenInput)



