from django.urls import path
from .views import ItemView, IndexView


app_name = 'catalog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/', ItemView.as_view(), name='catalog'),
]