# coding=utf-8
from django.db import models


class Settings(models.Model):
    title = models.CharField("Название сайта", max_length=200)
    description = models.TextField("Описание сайта", max_length=200)
    phone_home = models.CharField("Тел. в шапке", max_length=200)
    email = models.CharField("E-mail", max_length=200)
    contacts = models.TextField("Контакты", blank=True)
    delivery = models.CharField("Доставка", max_length=200, blank=True)
    pay = models.CharField("Оплата", max_length=200, blank=True)
    recovery = models.CharField("Возврат", max_length=200, blank=True)
    terms = models.CharField("Условия", max_length=200, blank=True)
    footer_link = models.TextField("Код счётчиков в футере", blank=True)