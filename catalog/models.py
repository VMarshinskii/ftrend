﻿# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    parent = models.ForeignKey("self", verbose_name="Родительская категория", blank=True, null=True, default="-1")
    step = models.IntegerField("Вложенность", blank=True, editable=False)
    products_count = models.IntegerField("Количество товаров", default=0, editable=False)
    text = models.TextField("Описание категории", blank=True, null=True, help_text="Текст на странице")
    url = models.CharField("Url", max_length=200, blank=True, unique=True)

    description = models.CharField("Description", max_length=200, blank=True, help_text="Небольшое seo описание страницы")
    keywords = models.CharField("Ключевые слова", max_length=200, blank=True, help_text="Клучевые слова (через запятую)")

    class Meta:
        verbose_name_plural = u"Категории"
        verbose_name = u"Категория"

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.parent is None:
            self.step = 0
        else:
            self.step = self.parent.step + 1
        super(Category, self).save(*args, **kwargs)

    def get_all_product(self):
        mass_product = []

        def rec_category(obj):
            product = Product.objects.filter(category=obj)
            for product in product:
                mass_product.append(product)
            categories = Category.objects.filter(parent=obj)
            for category in categories:
                rec_category(category)

        rec_category(self)
        return mass_product

    def get_path_categ(self):
        mass_pass = []

        def rec_path(obj):
            if obj is not None:
                mass_pass.append(obj)
                rec_path(obj.parent)

        rec_path(self)
        return mass_pass


COLORS = (
    ('Белый', 'Белый'),
    ('Жёлтый', 'Жёлтый'),
    ('Зелёный', 'Зелёный'),
    ('Красный', 'Красный'),
)


class Color(models.Model):
    title = models.CharField("Название", max_length=200)

    class Meta:
        verbose_name_plural = "Цвета"
        verbose_name = "Цвет"

    def __unicode__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField("Название", max_length=200)
    text = models.TextField("Описание", blank=True, null=True)
    url = models.CharField("Url", max_length=200, blank=True)

    description = models.CharField("Description", max_length=200, blank=True, help_text="Небольшое seo описание страницы")
    keywords = models.CharField("Ключевые слова", max_length=200, blank=True, help_text="Клучевые слова (через запятую)")

    class Meta:
        verbose_name_plural = "Бренды"
        verbose_name = "Бренд"

    def __unicode__(self):
        return self.title


AGE_CHOICES = (('boys', 'Мальчики'),
               ('girls', 'Девочки'))

List = {'boys': 'Мальчики', 'girls': 'Девочки'}


class Age(models.Model):
    type = models.CharField("Для кого", max_length=200, choices=AGE_CHOICES, default='boys')
    title = models.CharField("Название", max_length=200)
    text = models.TextField("Описание", blank=True, null=True)
    url = models.CharField("Url", max_length=200, blank=True)

    description = models.CharField("Description", max_length=200, blank=True, help_text="Небольшое seo описание страницы")
    keywords = models.CharField("Ключевые слова", max_length=200, blank=True, help_text="Клучевые слова (через запятую)")

    class Meta:
        verbose_name_plural = "Возраст"
        verbose_name = "Возраст"

    def __unicode__(self):
        if str(self.type) == 'boys':
            return u"Для мальчиков " + " " + self.title
        return u"Для девочек " + " " + self.title

    def name(self):
        if self.type == 'boys':
            str_name = u"Для мальчиков " + self.title
            str_name = str_name.encode('utf-8')
            return str_name
        else:
            str_name = u"Для девочек " + self.title
            str_name = str_name.encode('utf-8')
            return str_name


class Collection(models.Model):
    title = models.CharField("Название", max_length=200)

    class Meta:
        verbose_name_plural = "Коллекции"
        verbose_name = "Коллекция"

    def __unicode__(self):
        return self.title


class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    price = models.IntegerField("Цена", default=0)
    price_sale = models.IntegerField("Цена со скидкой", default=0, editable=False)
    code = models.CharField("Артикул", max_length=200, blank=True)
    category = models.ForeignKey(Category, verbose_name="Категория", blank=True, null=True)
    sale_value = models.IntegerField("Скидка, %", default=0)
    sale_status = models.BooleanField("Сделать скидку", default=False)
    sizes = models.CharField("Размеры", max_length=200, blank=True)
    size_colors = models.TextField("Цвета размеров", blank=True)
    colors = models.ManyToManyField(Color, verbose_name="Цвета", blank=True)
    age = models.ManyToManyField(Age, verbose_name="Возраст", blank=True)
    brand = models.ForeignKey(Brand, verbose_name="Бренд", blank=True, null=True, on_delete=models.SET_NULL)
    collection = models.ManyToManyField(Collection, verbose_name="Коллекция", blank=True)
    text = models.TextField("Описание")
    image = models.CharField("Изображение", max_length=200, blank=True)
    images = models.CharField("Изображения", max_length=250, blank=True)
    country = models.CharField("Страна производства", max_length=250, blank=True)
    included = models.CharField("В комплекте", max_length=250, blank=True)
    structure = models.CharField("Состав", max_length=250, blank=True)
    keywords = models.CharField("Ключевые слова", max_length=200)
    description = models.CharField("Description", max_length=200)
    similar = models.ManyToManyField("self", verbose_name="Похожие товары", blank=True)
    date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    novelty = models.BooleanField("Новинки", default=False)
    sell = models.BooleanField("Рекомендуемые", default=False)
    popular_count = models.IntegerField("Популярность", default=0)

    is_active = models.BooleanField("Видимость", default=True)

    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"

    def __unicode__(self):
        return self.name

    def get_price(self):
        if self.sale_status:
            return self.price_sale
        return self.price

    def save(self, *args, **kwargs):
        if self.sale_status is True:
            self.price_sale = self.price / 100.0 * (100.0 - self.sale_value)
        super(Product, self).save(*args, **kwargs)

    def get_prew(self):
        image = u'<img src="/uploads/' + str(self.image) + u'" style="height:40px"/>'
        return "sdsa".encode('utf-8')

    # get_prew.allow_tags = True
    get_prew.short_description = 'Изображение'
