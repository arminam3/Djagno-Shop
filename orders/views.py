from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext as __
from django.http import  HttpResponseRedirect

from .models import Order, ProductOrder
from . forms import OrderCreationForm
from cart.cart import Cart

from gateways.views import go_to_gateway_view


def order_detail_view(request):
    return render(request, 'orders/checkout.html')

class OrderCreateView(LoginRequiredMixin, CreateView):
    form_class = OrderCreationForm
    template_name = 'orders/checkout.html'
    # success_url = reverse_lazy('product:list')

    def get_success_url(self):
        if 'pay' in self.request.POST:
            # messages.sucordercess(
            #     self.request,
            # __('Your order has been successfully registered')
            #     )
            # go_to_gateway_view(self.request)
            return reverse('go_to_gateway', args=[self.object.pk])
        return reverse('account:profile_detail_update')

    def get_form_kwargs(self):
        kwargs = super(OrderCreateView, self).get_form_kwargs()
        kwargs.update(
            {'user': self.request.user}
        )
        return kwargs

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=False)
        obj.user = self.request.user
        cart = Cart(self.request)
        obj.save()
        for item in cart:
            if item.get('product_obj'):
                product_order = ProductOrder.objects.create(product=item['product_obj'], quantity=item['quantity'])
                obj.products.add(product_order)
                cart.remove(item['product_obj'], send_message=False)

        return super(OrderCreateView, self).form_valid(form)