# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField


class Page(models.Model):
    title = models.CharField("Название", max_length=200)
    text = RedactorField(verbose_name="Текст")
    url = models.CharField("Url", max_length=200, default='', unique=True)
    description = models.CharField("Description", max_length=200, blank=True)
    keywords = models.CharField("Keywords", max_length=200, blank=True)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __unicode__(self):
        return self.title