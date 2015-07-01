# -*- coding: utf-8 -*-
from django.db import models
from catalog.models import Product


class Cart(models.Model):
    hash = models.CharField("Хеш", max_length=200)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, verbose_name="Корзина", null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, verbose_name="Товар")
    count = models.IntegerField("Количество", blank=True)
    size = models.CharField("Размер", max_length=200, blank=True)
    color = models.CharField("Цвет", max_length=200, blank=True)
    price_order = models.IntegerField("Цена при заказе", default=0)
    image = models.CharField(verbose_name="Картинка", max_length=250, blank=True)
    title = models.CharField(verbose_name="Название", max_length=250, blank=True)



