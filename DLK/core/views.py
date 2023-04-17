from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView
from .forms import LoginForm, SignUpForm
from .models import CustomUser
from django.views import View
from django.contrib.auth import login


class IndexView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'core/login.html'
    redirect_authenticated_user = True

    def get_default_redirect_url(self, is_active=True, is_staff=True):
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


class CustomLogoutView(LogoutView):
    http_method_names = ['post', ]

    def get_default_redirect_url(self):
        return reverse('core:login')


class SignUpView(View):
    template_name = 'core/signup.html'
    form = SignUpForm

    def get_context_data(self):
        context = {
            'form': self.form,
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, request.FILES)
        context = self.get_context_data()
        context['form'] = form
        if form.is_valid():
            user = form.save()
            login(request, user)
            user_id = self.request.user.id
            return redirect(reverse('core:user_profile', kwargs={'user_id': user.id}))
        else:
            return render(request, self.template_name, context)

