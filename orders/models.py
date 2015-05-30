# -*- coding: utf-8 -*-
from django.db import models
from account.models import User
from cart.models import CartProduct


STAUSES = (
    (0, "В обработке"),
    (1, "Ждёт оплаты"),
)


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь")
    sum = models.IntegerField("Сумма заказа", default=0)
    status = models.IntegerField("Статус заказа", )

    first_name = models.CharField("Имя", max_length=200, default="")
    patronymic = models.CharField("Отчество", max_length=200, default="")
    last_name = models.CharField("Фамилия", max_length=200, default="")
    email = models.CharField("Email", max_length=200, default="")
    phone = models.CharField("Телефон", max_length=200, default="")
    city = models.CharField("Город", max_length=200, default="")
    address = models.TextField("Адрес")

    delivery = models.CharField("Доставка", max_length=200, default="")
    delivery_price = models.IntegerField("Стоимость доставки")

    date_create = models.DateField("Дата создания заказа", auto_now_add=True)
    date_now = models.DateField("Дата редактирования", auto_now=True)

    products = models.ManyToManyField(CartProduct, verbose_name="Товары")
