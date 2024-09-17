"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from azbankgateways.urls import az_bank_gateways_urls

from gateways.views import go_to_gateway_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('accounts.urls')),
    path('', include('pages.urls')),
    path('products/', include('products.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('gateways/', include('gateways.urls')),
    path('bankgateways/', az_bank_gateways_urls()),
    path('go_to_gateway/<int:pk>/', go_to_gateway_view, name='go_to_gateway'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
