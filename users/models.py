from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to="media/users/avatar", null=True, blank=True, verbose_name="آواتار")
    mobile = models.CharField(max_length=15, null=True, blank=True, verbose_name="موبایل")
    address = models.TextField(max_length=240, null=True, blank=True, verbose_name="آدرس")
