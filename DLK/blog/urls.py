from django.urls import path
from .views import ItemView, IndexView


app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/', ItemView.as_view(), name='blog'),
]