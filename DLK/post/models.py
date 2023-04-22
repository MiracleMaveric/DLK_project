from django.db import models
from core.models import CustomUser
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE)
    date_pub = models.DateTimeField(default=timezone.now())
    date_edit = models.DateTimeField(default=timezone.now())
    description = models.TextField(max_length=500, blank=False)
    likes = models.ManyToManyField(CustomUser, related_name='liked_posts', blank=True)

    def __str__(self):
        return f"Views from {self.author.username}"

    @property
    def get_likes(self):
        return self.likes.count()

