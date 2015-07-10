# -*- coding: utf-8 -*-
from django.db import models


class DeliveryCDEK(models.Model):
    name = models.CharField(verbose_name="Название", max_length=250)
    code = models.CharField(verbose_name="Код пункта выдачи", max_length=250)
    address = models.CharField(verbose_name="Адрес", max_length=250)
    phone = models.CharField(verbose_name="Телефон", max_length=250)
    mail = models.CharField(verbose_name="Почта", max_length=250)
    time = models.CharField(verbose_name="Время работы", max_length=250)
    url = models.CharField(verbose_name="Url", max_length=250, blank=True)

    class Meta:
        verbose_name = "Пункт выдачи"
        verbose_name_plural = "Пункты выдачи"

    def __unicode__(self):
        return self.name
