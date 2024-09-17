from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
# from django.utils.translation import
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddProductToCartForm



class ProductListView(generic.ListView):
    # model = Product
    template_name = 'products/product_list.html'
    queryset = Product.not_deleted.all()
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    queryset = Product.objects.filter(delete=False)
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        context['cart_form'] = AddProductToCartForm


        return context


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    # template_name = 'products/product_list.html'

    def get_success_url(self):
        messages.success(
            self.request,
            "نظر شما با موفقیت ثبت شد"
        )
        return reverse('product:detail', args=[self.kwargs['pk']])

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        obj.product = product
        obj.save()
        return super(CommentCreateView, self).form_valid(form)




