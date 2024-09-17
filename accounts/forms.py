from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

from allauth.account.forms import UserForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'money',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = UserChangeForm.Meta.fields


class CustomUserUpdateProfileForm(CustomUserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    dramatic_name = forms.CharField(max_length=100, required=False)

