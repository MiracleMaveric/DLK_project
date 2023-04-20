from django.shortcuts import render
from django.views.generic.base import TemplateView


def toys(request):
    return render(request, 'toys.html')


class IndexView(TemplateView):
    template_name = 'toys.html'


class ItemView(TemplateView):
    template_name = 'index.html'
