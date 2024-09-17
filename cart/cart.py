from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib import messages
from django.utils.translation import gettext as _
import requests as req


from kavenegar import *



class Cart:
    def __init__(self, request):
        """
        Initialize The Cart
        """
        self.request = request
        self.session = request.session

        cart = request.session.get('cart')

        if not cart:
            cart = request.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity=1, replace_quantity=False):
        """
        Add A Product To Cart OR Increase It's quantity
        """
        product_id = str(product.id)
        cart = self.cart

        if not product_id in cart:
            cart[product_id] = {'quantity': 0}

        if replace_quantity:
            cart[product_id]['quantity'] = quantity
        else:
            cart[product_id]['quantity'] += quantity


        self.save()
        messages.success(
            self.request,
            _("Successfully done")
        )

    def remove(self, product, send_message=True):
        """
        Remove a product from cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            if send_message:
                messages.success(
                    self.request,
                    _("Product successfully removed")
                )

        self.save()


    def save(self):
        """
        Save Changes In Session
        """
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids, delete=False)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product
            # print('product is in products')

        product_list = []
        for item in cart.values():
            if product := item.get('product_obj'):
                if not product.delete:
                    item['total_price_by_quantity'] = item['quantity'] * item['product_obj'].price
                    yield item



    def length(self):
        """
        get the len of products in cart that NOT deleted ( not important it is active or not)
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        # for product in products:

        return sum(item['quantity'] if item.get('product_obj').active else 0 for item in self.cart.values())

    def clear(self):
        del self.session['cart']

        messages.success(
            self.request,
            _("Successfully done")
        )

        self.save()

    def get_total_price(self):
        """
        get total price of products in cart that
        """
        product_ids = self.cart.keys()
        # products = Product.objects.filter(id__in=product_ids, active=True)
        total = 0
        for product_id in self.cart:
            product = get_object_or_404(Product, id=int(product_id))
            quantity = self.cart[product_id]['quantity']
            if product.active:
                total += quantity * product.price
        return total


        # return sum(item['product_obj'].price * item['quantity'] for item in self.cart.values())
