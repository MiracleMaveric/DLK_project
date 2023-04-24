from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin, UserCreationForm
from ..blog.models import Post

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Post)
