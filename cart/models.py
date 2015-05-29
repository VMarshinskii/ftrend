# -*- coding: utf-8 -*-
from django.db import models
from catalog.models import Product


class Cart(models.Model):
    hash = models.CharField("Хеш", max_length=200)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, verbose_name="Корзина", null=True)
    product = models.ForeignKey(Product, verbose_name="Товар")
    count = models.IntegerField("Количество", blank=True)
    size = models.CharField("Размер", max_length=200, blank=True)
    color = models.CharField("Цвет", max_length=200, blank=True)



