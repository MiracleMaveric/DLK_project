from django.shortcuts import render
from django.views.generic.base import TemplateView


def catalog(request):
    return render(request, 'catalog.html')


class IndexView(TemplateView):
    template_name = 'catalog.html'


class ItemView(TemplateView):
    template_name = 'index.html'