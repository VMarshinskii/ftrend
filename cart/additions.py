# -*- coding: utf-8 -*-
from models import Cart, CartProduct
from ftrend.additions import random_str


def get_cart(request):
    if 'cart_hash' in request.session:
        cart_hash = request.session['cart_hash']
        try:
            return Cart.objects.get(hash=cart_hash)
        except Cart.DoesNotExist:
            pass
    cart = Cart()
    cart.hash = random_str(25)
    cart.save()
    request.session['cart_hash'] = cart.hash
    return cart


def get_sum(request):
    cart = get_cart(request)
    products = CartProduct.objects.filter(cart=cart)
    summa = 0
    for product in products:
        if product.product.sale_status:
            summa += product.product.price_sale * product.count
        else:
            summa += product.product.price * product.count
    return summa


def get_count(request):
    cart = get_cart(request)
    products = CartProduct.objects.filter(cart=cart)
    count = 0
    for product in products:
        count += product.count
    return count
