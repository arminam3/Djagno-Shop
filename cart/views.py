from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext as _



from products.models import Product
from .forms import AddProductToCartForm
from kavenegar import *

from .cart import Cart

def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['product_update_quantity_form'] = AddProductToCartForm(initial={
            'replace_quantity': True,
            'quantity': item['quantity']
        })

    context = {
        'cart': cart,
    }
    for j in cart:
        print(j)
    return render(request, 'cart/cart.html', context)

@require_POST
def add_to_cart_view(request, pk):
    cart = Cart(request)
    cart_form = AddProductToCartForm(request.POST)

    if cart_form.is_valid():
        product = get_object_or_404(Product, id=pk, active=True)

        cleaned_data = cart_form.cleaned_data
        quantity = cleaned_data['quantity']
        replace_quantity = cleaned_data['replace_quantity']
        cart.add(product, quantity=quantity, replace_quantity=replace_quantity)

        return redirect('cart:detail')
    return Http404

def remove_from_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    return redirect('cart:detail')
