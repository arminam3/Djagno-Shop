from django.urls import path

from .views import (
    cart_detail_view, add_to_cart_view,
    remove_from_cart_view,
    # number_of_product_in_cart_equal_view,
    )

app_name = 'cart'

urlpatterns = [
    path('', cart_detail_view, name='detail'),
    path('add/<int:pk>', add_to_cart_view, name='add'),
    path('remove/<int:product_id>', remove_from_cart_view, name='remove'),
    # path('checkout/', checkout_view, name='checkout'),
    # path('equal/<int:product_id>', number_of_product_in_cart_equal_view, name='equal'),
]
