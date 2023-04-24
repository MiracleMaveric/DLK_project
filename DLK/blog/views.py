from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from DLK.blog.models import Post


def blog(request):
    return render(request, 'blog.html')


class IndexView(TemplateView):
    template_name = 'blog.html'


class ItemView(TemplateView):
    template_name = 'index.html'

def show_posts(request):
    posts = Post.objects.all()
    result = [f"Author: {post.author} Date: {post.date_pub} Description: {post.description}\n" for post in posts]
    return HttpResponse(result)

def post_detail(request, post_id):
    return HttpResponse(f"Post id: {post_id}")

def post_create(request):
    return HttpResponse('Create post')

def post_update(request, post_id):
    return HttpResponse(f"Update post id: {post_id}")

def post_delete(request, post_id):
    return HttpResponse(f"Delete post id: {post_id}")

def post_like(request, post_id):
    return HttpResponse(f"Like post id: {post_id}")

