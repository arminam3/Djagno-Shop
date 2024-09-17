from atexit import register
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_editable = ['email']

    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]["fields"] += ('dramatic_name', 'phone', 'address', "money",)

    add_fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'dramatic_name',
                'phone',
                'address',
                'money',
            ),
        }),
    )


