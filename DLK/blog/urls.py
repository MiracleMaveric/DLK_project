from django.urls import path
from .views import ItemView, IndexView, post_detail, post_create, post_update, post_delete, post_like, show_posts

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/', ItemView.as_view(), name='blog'),
    path('detail/<int:post_id>/', post_detail, name='detail'),
    path('create/', post_create, name='create'),
    path('update/<int:post_id>/', post_update, name='update'),
    path('delete/<int:post_id>/', post_delete, name='delete'),
    path('like/<int:post_id>/', post_like, name='like'),
    path('show_posts/', show_posts, name='show'),
]