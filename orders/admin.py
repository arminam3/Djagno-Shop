from django.contrib import admin
from django.utils.translation import gettext as __ , gettext_lazy as _

from .models import Order, ProductOrder


# class ProductOrderInline(admin.TabularInline):
#     model = ProductOrder.order.through
#     fields = ['product', 'quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'phone', 'email', 'payment_status', 'payment_boolean_status', 'j_datetime_created', ]
    readonly_fields = ['datetime_created', 'datetime_modified']
    # list_filter = ['payment_status']

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)
    get_full_name.short_description = _('name and family')


    Order.payment_status.short_description = _('payment_status')


    Order.payment_boolean_status.boolean = True
    Order.payment_boolean_status.short_description = _('payment_boolean_status')

    Order.j_datetime_created.short_description = _('j_datetime_created')



@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ['product', ]