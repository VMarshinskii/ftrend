# -*- coding: utf-8 -*-
from models import Cart
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
