from django.contrib import admin

from .models import Product, Comment


# class ProductCommentInline(admin.StackedInline):
class ProductCommentInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'stars', 'active']
    extra = 1


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'price', 'active']
#     list_editable = ['active']
#     inlines = [
#         ProductCommentInline,
#     ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'stars', 'active']
    list_editable = ['active']


from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


# class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
#     model = SecendModel
#
#
# class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
#     model = ThirdModel


@admin.register(Product)
class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    # show jalali date in list display
    list_display = ['title', 'price', 'active', 'delete', 'j_datetime_created']
    list_editable = ['price', 'active', 'delete']

    # inlines = (MyInlines1, MyInlines2,)
    # raw_id_fields = ('some_fields',)
    # readonly_fields = ('some_fields', 'date_field',)
    # you can override formfield, for example:
    # formfield_overrides = {
    #     JSONField: {'widget': JSONEditor},
    # }

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.datetime_created).strftime('%y/%m/%d _ %H:%M:%S')

    get_created_jalali.short_description = 'تاریخ ایجاد'
    get_created_jalali.admin_order_field = 'created'


