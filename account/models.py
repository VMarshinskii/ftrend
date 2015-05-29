# coding=utf-8
from django.contrib.auth.models import AbstractUser
from django.db import models
# from catalog.models import Video

# Модифицируем поле email.
AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False
AbstractUser._meta.get_field('email').default = ""
AbstractUser._meta.get_field('first_name').blank = False
AbstractUser._meta.get_field('first_name').default = ""


class User(AbstractUser):
    address = models.CharField("Адрес", max_length=250)