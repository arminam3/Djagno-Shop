from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, FormView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext as __, gettext_lazy as _

from allauth.account.forms import ChangePasswordForm
from allauth.account.views import PasswordChangeView


from .forms import CustomUserCreationForm, CustomUserUpdateProfileForm
from orders.models import Order
from .mixins import TrueUserMixin


class RegisterView(CreateView):
    model = get_user_model()
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('account:home')


# class ProfileDetailView(LoginRequiredMixin, DetailView):
#     model = get_user_model()
#     template_name = 'accounts/profile_information.html'
#     form_class = CustomUserUpdateProfileForm
#
#     # def get_form_kwargs(self):
#     #     kwargs = super(ProfileDetailView, self).get_form_kwargs()
#     #     kwargs.update(
#     #         {'user': self.request.user}
#     #     )
#     #     return kwargs
#
#     def form_valid(self, form):
#         # form.instance.username = self.request.user
#         return super(ProfileDetailView, self).form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super(ProfileDetailView, self).get_context_data(**kwargs)
#         context['profile_form'] = CustomUserUpdateProfileForm
#         return context
#
#     def get_success_url(self):
#
#         return reverse('account:profile_detail', args=[self.request.user.pk])

@login_required()
def profile_info_update_view(request):
    """
    POST method update user info
    """
    user = request.user
    if request.method == 'POST':
        profile_form = CustomUserUpdateProfileForm(request.POST)

        if profile_form.is_valid():
            alike_username = get_user_model().objects.filter(username=profile_form.cleaned_data['username'])
            if user in alike_username:
                messages.error(
                    request,
                    __('This Username has been selected by another user')
                )

            else:
                # if not user.username == profile_form.cleaned_data['username']:
                #     user.username = profile_form.cleaned_data['username']

                user.first_name = profile_form.cleaned_data['first_name']
                user.last_name = profile_form.cleaned_data['last_name']
                user.dramatic_name = profile_form.cleaned_data['dramatic_name']

                user.save()


        else:
            profile_form = CustomUserUpdateProfileForm(request.POST)
            messages.error(
                request,
                __('Please complete form correctly')
            )

    else:
        profile_form = CustomUserUpdateProfileForm(instance=user)

    return render(request, 'accounts/profile_information.html', {'profile_form': profile_form})







# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = get_user_model()
#     form_class = CustomUserUpdateProfileForm
#
#     def get_success_url(self):
#         return reverse('account:profile_detail', args=[self.request.user.pk])








