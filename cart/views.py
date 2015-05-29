# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse
from catalog.models import Product
from cart.models import CartProduct
from forms import CartProductForm
from additions import get_cart


def cart_index_view(request):
    cart = get_cart(request)
    cart_sum = 0
    product_carts = []

    for product_cart in CartProduct.objects.filter(cart=cart):
        product = product_cart
        product.sum = product_cart.product.price * product_cart.count
        cart_sum += product_cart.product.price * product_cart.count
        product_carts.append(product)

    return render_to_response("cart_index.html", {
        'user': request.user,
        'product_carts': product_carts,
        'sum': cart_sum
    })


def add_product_ajax(request):
    if request.POST:
        cart = get_cart(request)
        form = CartProductForm(request.POST)
        cart_product = form.save(commit=False)
        try:
            cart_product.product = Product.objects.get(id=int(request.POST.get('product_id', -1)))
            cart_product.cart = cart
            cart_product.save()
            return HttpResponse("Товар добавлен в корзину")
        except Product.DoesNotExist:
            pass
    return HttpResponse("Ошибка")


def count_product_ajax(request):
    if request.POST:
        cart_product_id = request.POST.get('product_id', -1)
        count = int(request.POST.get('count', 1))
        try:
            cart_product = CartProduct.objects.get(id=cart_product_id)
            new_count = cart_product.count + count
            cart_product.count = new_count
            cart_product.save()
            if new_count < 1:
                cart_product.delete()
        except CartProduct.DoesNotExist:
            pass

    cart = get_cart(request)
    cart_sum = 0
    product_carts = []

    for product_cart in CartProduct.objects.filter(cart=cart):
        product = product_cart
        product.sum = product_cart.product.price * product_cart.count
        cart_sum += product_cart.product.price * product_cart.count
        product_carts.append(product)

    return render_to_response("cart_index_ajax.html", {
        'product_carts': product_carts,
        'sum': cart_sum
    })

