from django.urls import path

from .custom_views import payment_view

app_name = 'gateway'

urlpatterns = [
    path('payment/<int:pk>', payment_view, name='payment'),
]
