# coding=utf-8
from django.db import models


class Settings(models.Model):
    title = models.CharField("Название сайта", max_length=200)
    description = models.TextField("Описание сайта", max_length=200)
    phone_home = models.CharField("Тел. в шапке", max_length=200)
    email = models.CharField("E-mail", max_length=200)
    contacts = models.TextField("Контакты", blank=True)
    odnoklassniki = models.CharField("Одноклассники", max_length=200, blank=True)
    twitter = models.CharField("Twitter", max_length=200, blank=True)
    facebook = models.CharField("Facebook", max_length=200, blank=True)
    vk = models.CharField("Вконтакте", max_length=200, blank=True)
    footer = models.TextField("Текст в футере", blank=True, default="qwe")
    footer_link = models.TextField("Код счётчиков в футере", blank=True)