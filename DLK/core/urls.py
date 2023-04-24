from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import CustomLoginView, IndexView, ProfileView, CustomLogoutView, SignUpView, SuggestionView, \
    ProfileEditView, CustomPasswordResetView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('user_profile/<int:user_id>/', ProfileView.as_view(), name='user_profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('suggestion/', SuggestionView.as_view(), name='suggestion'),
    path('edit_profile/<int:user_id>/', login_required(ProfileEditView.as_view()), name='edit_profile'),
    path('password_reset/', login_required(CustomPasswordResetView.as_view()), name='password_reset'),
]