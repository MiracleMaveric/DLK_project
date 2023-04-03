from django.urls import path
from .views import CustomLoginView, IndexView, ProfileView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('user_profile/<int:user_id>/', ProfileView.as_view(), name='user_profile'),
]