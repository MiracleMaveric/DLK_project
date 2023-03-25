from django.shortcuts import render
from django.views.generic.base import TemplateView


def blog(request):
    return render(request, 'blog.html')


class IndexView(TemplateView):
    template_name = 'index.html'


class ItemView(TemplateView):
    template_name = 'blog.html'