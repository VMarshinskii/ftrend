# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse, redirect, get_object_or_404, render
from django.core.context_processors import csrf
from django.contrib import auth
from forms import OrderForm
from ftrend.additions import translit, random_str
from models import DeliveryType, Order
from cart.additions import get_cart, get_sum
from cart.models import CartProduct
from account.models import User


STAUSES = ["В обработке", "Ждёт оплаты"]


def create_order(request):
    args = {
        'form': OrderForm(),
        'delivery_mass': DeliveryType.objects.all(),
        'user': request.user,
        'user_active': request.user.is_authenticated(),
        'cart_sum': get_sum(request),
    }
    args.update(csrf(request))
    is_valid = True

    if request.user.is_authenticated():
        ord = Order()
        ord.first_name = request.user.first_name
        ord.last_name = request.user.last_name
        ord.email = request.user.email
        ord.phone = request.user.phone
        ord.city = request.user.city
        ord.address = request.user.address
        args['form'] = OrderForm(instance=ord)

    if request.POST:
        if request.POST.get('first_name', "") == "":
            args['user_inform_error'] = True
            args['first_name_error'] = "error_field"
            is_valid = False
        if request.POST.get('last_name', "") == "":
            args['user_inform_error'] = True
            args['last_name_error'] = "error_field"
            is_valid = False
        if request.POST.get('email', "") == "":
            args['user_inform_error'] = True
            args['email_error'] = "error_field"
            is_valid = False
        if request.POST.get('phone', "") == "":
            args['user_inform_error'] = True
            args['phone_error'] = "error_field"
            is_valid = False

        if request.POST.get('city', "") == "":
            args['address_inform_error'] = True
            args['city_error'] = "error_field"
            is_valid = False
        if request.POST.get('address', "") == "":
            args['address_inform_error'] = True
            args['address_error'] = "error_field"
            is_valid = False

        if request.POST.get('delivery', "") == "":
            args['delivery_error'] = "выберите тип доставки"
            args['delivery_error'] = "error_field"
            is_valid = False

        if 'register' in request.POST:
            try:
                email = request.POST.get('email', "")
                User.objects.get(email=email)
                args['register_error'] = "Пользователь с таким email уже разегистрирован"
                is_valid = False
            except User.DoesNotExist:
                pass

        form = OrderForm(request.POST)
        if is_valid and form.is_valid():
            order = form.save(commit=False)
            delivery = DeliveryType.objects.get(id=request.POST['delivery'])
            order.delivery = delivery.title
            order.delivery_price = delivery.price
            order.status = 0
            print(get_sum(request))
            order.sum = get_sum(request)
            if request.user.is_authenticated():
                order.user = request.user
            order.save()
            cart = get_cart(request)
            if cart:
                for pr in CartProduct.objects.filter(cart=cart):
                    if pr.product.sale_status:
                        pr.price_order = pr.product.price_sale
                    else:
                        pr.price_order = pr.product.price
                    pr.save()
                    order.products.add(pr)
            else:
                args['cart_error'] = "в вашей корзине ничего нет"
            order.save()

            if 'register' in request.POST:
                new_user = User()
                new_user.first_name = request.POST.get('first_name', "")
                new_user.last_name = request.POST.get('last_name', "")
                new_user.email = request.POST.get('email', "")
                new_user.phone = request.POST.get('phone', "")
                new_user.city = request.POST.get('city', "")
                new_user.address = request.POST.get('address', "")
                new_user.username = translit(new_user.first_name) + "_" + random_str(6)
                password = random_str(7)
                new_user.set_password(password)
                new_user.save()
                # отправка уведомления
                user = auth.authenticate(username=new_user.username, password=password)
                if user is not None and user.is_active:
                    auth.login(request, user)
                return redirect("/orders/reg_thanks/")
            elif request.user.is_authenticated():
                request.user.last_name = request.POST.get('last_name', "")
                request.user.first_name = request.POST.get('first_name', "")
                request.user.phone = request.POST.get('phone', "")
                request.user.city = request.POST.get('city', "")
                request.user.address = request.POST.get('address', "")
                request.user.save()

            return redirect("/orders/thanks/")

        args['form'] = form
    return render_to_response("create_order.html", args)


def thank_order(request):
    return render_to_response("thank_order.html")

def reg_thank_order(request):
    return render_to_response("thank_register_order.html")


def orders_view(request):
    if request.user.is_authenticated():
        orders = []

        for order in Order.objects.filter(user=request.user):
            order.status_title = STAUSES[order.status]
            order.sum += order.delivery_price
            orders.append(order)

        return render_to_response("orders.html", {'orders': reversed(orders)})

    return redirect("/authentication/")

def order_view(request, id=-1):
    if request.user.is_authenticated():
        try:
            order = Order.objects.get(id=id)
            products = []

            for product in order.products.all():
                product.sum = product.price_order * product.count
                products.append(product)

            return render_to_response("order.html", {
                'order': order,
                'status': STAUSES[order.status],
                'products': products,
            })
        except Order.DoesNotExist:
            pass

    return redirect("/authentication/")
