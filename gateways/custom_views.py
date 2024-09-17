from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.utils.translation import gettext as __

from azbankgateways.models import Bank

from orders.models import Order

def payment_view(request, pk):
    """
    Choose a payment for a order
    """
    if request.method == 'GET':
        order = get_object_or_404(Order, pk=pk)

        tracking_code = int(request.GET.get('tc'))
        payment = get_object_or_404(Bank, tracking_code=tracking_code)

        order.payment = payment
        order.save()

        if payment.get_status_display() == 'Complete':
            messages.success(
                request,
                __('Your bill has been successfully paid')
            )
        else:
            messages.error(
                request,
                __('Your bill has not been  paid')
            )

        return redirect(reverse('product:list'))

    return Http404
