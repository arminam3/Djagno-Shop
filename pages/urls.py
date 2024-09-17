from django.urls import path

from .views import AboutUs, HomeView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about-us/', AboutUs.as_view(), name='about_us'),

]
