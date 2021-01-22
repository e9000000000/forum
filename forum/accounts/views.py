from django.views.generic import UpdateView, DetailView, UpdateView
from django_registration.backends.activation.views import RegistrationView
from django.urls import reverse_lazy

from . import models
from .models import User


class ProfileDetailView(DetailView):
    """
    Display a :model:`auth.User`.
    """
    model = User
    context_object_name = 'account'
    template_name = 'accounts/profile.html'

class ProfileUpdateView(UpdateView):
    """
    Display form to update a :model:`auth.User`.
    """
    model = User
    context_object_name = 'account'
    template_name = 'accounts/profile_edit.html'
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'bio',
        'avatar',
    ]

    def get_success_url(self):
        return reverse_lazy(
            'profile',
            kwargs={
                'pk': self.object.pk
            }
        )

    def get_object(self):
        return self.request.user