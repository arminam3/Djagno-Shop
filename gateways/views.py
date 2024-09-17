from django.shortcuts import render,get_object_or_404

from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings

from orders.models import Order


def go_to_gateway_view(request, pk):
    # خواندن مبلغ از هر جایی که مد نظر است
    # convert tooman to rial by * in 10
    amount = get_object_or_404(Order, pk=pk).get_total_price_by_quantity()*10
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = '+989112221234'  # اختیاری

    factory = bankfactories.BankFactory()
    bank = factory.create()  # or factory.create(bank_models.BankType.BMI) or set identifier
    bank.set_request(request)
    bank.set_amount(amount)
    # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
    bank.set_client_callback_url(reverse('gateway:payment', args=[pk, ]))
    bank.set_mobile_number(user_mobile_number)  # اختیاری

    # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
    # پرداخت برقرار کنید.
    bank_record = bank.ready()

    # هدایت کاربر به درگاه بانک
    return bank.redirect_gateway()






