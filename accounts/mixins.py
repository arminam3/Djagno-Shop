from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import Http404

class TrueUserMixin:
    def dispatch(self):
        user = get_object_or_404(get_user_model(), pk=self.kwargs.get('pk'))
        if self.request.user != user:
            return Http404
        return super(UserIsCorrectMixin, self).dispatch()
            