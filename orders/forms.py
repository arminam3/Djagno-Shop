from django import forms

from .models import Order

class OrderCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(OrderCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['value'] = user.first_name
        self.fields['first_name'].widget.attrs['class'] = 'form-input form__input--2'
        self.fields['last_name'].widget.attrs['value'] = user.last_name
        self.fields['last_name'].widget.attrs['class'] = 'form__input form__input--2'
        self.fields['address'].widget.attrs['value'] = user.address if user.address else ''
        self.fields['address'].widget.attrs['class'] = 'form__input form__input--2'
        self.fields['phone'].widget.attrs['value'] = user.phone if user.phone else ''
        self.fields['phone'].widget.attrs['class'] = 'form__input form__input--2'
        self.fields['email'].widget.attrs['value'] = user.email if user.email else ''
        self.fields['email'].widget.attrs['class'] = 'form__input form__input--2'


    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'email', 'phone', 'note',)


