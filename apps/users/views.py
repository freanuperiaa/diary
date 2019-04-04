from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from .models import CustomUser
from .forms import CustomUserCreationForm


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


class ProfileView(DetailView):
    model = CustomUser

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(username=
                                          self.request.user.username)
