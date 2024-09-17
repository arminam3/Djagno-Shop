from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator

from azbankgateways.models import Bank

from products.models import Product
from extensions.utils import jalali_convertor

class Order(models.Model):
    class Meta:
        ordering = ['-datetime_created']
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    NUMBERS = RegexValidator(r'^[0-9]')

    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='order', verbose_name=_('User'))
    first_name = models.CharField(max_length=50, verbose_name=_('name'))
    last_name = models.CharField(max_length=50, verbose_name=_('family'))
    address = models.CharField(max_length=300, verbose_name=_('address'))
    phone = models.CharField(max_length=11, validators=[NUMBERS], verbose_name=_('phone'))
    email = models.EmailField(verbose_name=_('email'))
    note = models.TextField(blank=True, verbose_name=_('note'))
    products = models.ManyToManyField('ProductOrder', related_name='order', verbose_name=_('products'))
    payment = models.OneToOneField(Bank,
                                blank=True,
                                null=True,
                                related_name='order',
                                verbose_name=_('payment'),
                                on_delete=models.SET_NULL
                                )

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def j_datetime_created(self):
        return jalali_convertor(self.datetime_created)

    def payment_status(self):
        if self.payment:
            return self.payment.status


    def payment_boolean_status(self):
        if self.payment:
            if self.payment.get_status_display() == 'Complete':
                return True
        return False


    def get_total_price_by_quantity(self):
        return sum(item.product.price * item.quantity for item in self.products.all())


class ProductOrder(models.Model):
    product = models.ForeignKey(Product,
                                related_name='product_order',
                                on_delete=models.PROTECT,
                                verbose_name=_('product'))
    quantity = models.PositiveIntegerField(_('quantity'))

    def __str__(self):
        return self.product.title