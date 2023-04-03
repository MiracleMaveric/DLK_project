from django.urls import path
from .views import ItemView, IndexView


app_name = 'user_profile'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('user_profile/<int:user_id>/', ItemView.as_view(), name='user_profile'),
]