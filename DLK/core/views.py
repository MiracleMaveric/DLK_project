from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView
from .forms import LoginForm
from .models import CustomUser


class IndexView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'core/login.html'
    redirect_authenticated_user = True

    def get_default_redirect_url(self):
        user_id = self.request.user.id
        return reverse('core:user_profile', kwargs={'user_id': user_id})




class ProfileView(DetailView):
    model = CustomUser
    template_name = 'core/user_profile.html'
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['header'] = f'Profile of {object.username}'
        return context

