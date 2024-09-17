from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from jalali_date import date2jalali, datetime2jalali
from ckeditor.fields import RichTextField

from extensions.utils import jalali_convertor


#-------- Managers ----------

class NotDeletedProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(delete=False)


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


# --------Models---------

class Product(models.Model):
    class Meta:
        ordering = ('-active',)

    title = models.CharField(max_length=100)
    short_description = models.TextField(blank=True)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    cover = models.ImageField(verbose_name=_('Product cover'), upload_to='product/product_cover', blank=True)
    delete = models.BooleanField(default=False)

    datetime_created = models.DateTimeField(_('DateTime of creation'), auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    #Managers
    objects = models.Manager()
    not_deleted = NotDeletedProductManager()

    #Methods - Cre
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.delete:
            self.active = False
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product:detail', args=[self.pk])

    def active_comments(self):
        return Comment.objects.filter(product=self, active=True)

    def j_datetime_created(self):
        return jalali_convertor(self.datetime_created)



class Comment(models.Model):
    class Meta:
        ordering = ['-datetime_created']

    PRODUCT_STARS = (
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name=_('Please Enter Your Idea'))
    stars = models.CharField(max_length=20, choices=PRODUCT_STARS, verbose_name=_('Stars'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    #Manager
    objects = models.Manager()
    active_product = ActiveCommentManager()

    def j_datetime_created(self):
        return jalali_convertor(self.datetime_created)

    def __str__(self):
        return f"{self.author }"

    def d_j_datetime_created(self):
        return datetime2jalali(self.datetime_created).strftime('%y/%m/%d _ %H:%M:%S')
