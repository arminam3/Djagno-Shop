from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator




class CustomUser(AbstractUser):
    NUMBERS = RegexValidator(r'^[0-9]')

    money = models.PositiveIntegerField(_('money'), default=0)
    phone = models.CharField(_('phone',), max_length=11, blank=True, null=True, validators=[NUMBERS])
    address = models.TextField(_('address'), blank=True, null=True)
    dramatic_name = models.CharField(_('dramatic name'), max_length=70, blank=True)
    # REQUIRED_FIELDS =zz []
