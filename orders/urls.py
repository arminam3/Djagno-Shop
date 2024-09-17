from django.urls import path

from .views import OrderCreateView, order_detail_view
app_name = 'order'

urlpatterns = [
    path('', order_detail_view, name='detail'),
    path('create/', OrderCreateView.as_view(), name='create'),

]
