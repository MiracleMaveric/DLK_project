from django.shortcuts import render
from django.views.generic.base import TemplateView


def ContactUs(request):
    return render(request, 'ContactUs.html')


class IndexView(TemplateView):
    template_name = 'ContactUs.html'


class ItemView(TemplateView):
    template_name = 'index.html'