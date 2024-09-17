from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic

from products.models import Product


# class HomeView(TemplateView):
#     template_name = "home.html"

class HomeView(generic.ListView):
    # model = Product
    template_name = 'products/product_list.html'
    queryset = Product.not_deleted.all()
    context_object_name = 'products'


class AboutUs(TemplateView):
    template_name = "pages/about_us.html"
