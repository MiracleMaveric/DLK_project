from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    birth_date = models.DateField(_('birth_date'), blank=True, null=True)
    phone = models.TextField(max_length=12, blank=True)
    email = models.TextField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='user_profile', blank=True)

    def __str__(self):
        return str(self.username)