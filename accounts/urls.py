from django.urls import path

from .views import profile_info_update_view

app_name = 'account'

urlpatterns = [
    path('detail/', profile_info_update_view, name='profile_detail_update'),
    # path('update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
]
