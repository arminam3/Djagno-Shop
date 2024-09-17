from importlib.metadata import PackagePath

from django.urls import path

from .views import ProductListView, ProductDetailView, CommentCreateView

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name="list"),
    path('detail/<int:pk>', ProductDetailView.as_view(), name="detail"),
    path('commnet/<int:pk>', CommentCreateView.as_view(), name="comment_create"),
]