# -*- coding: utf-8 -*-
from django.db import models
from catalog.models import Product


class Sale(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.CharField("Описание", max_length=200)
    text = models.TextField("Текст акции")
    image = models.ImageField("Изображение", upload_to='static/uploads/', blank=True)
    datetime = models.DateTimeField("Дата окончания")
    products = models.ManyToManyField(Product, verbose_name="Товары")
    url = models.CharField("Url", max_length=200, default='')
    is_active = models.BooleanField("Видимость", default=True)

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __unicode__(self):
        return self.title
