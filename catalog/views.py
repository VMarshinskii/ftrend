# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import Http404, HttpResponse
from django.middleware.csrf import get_token
from django.template import RequestContext
from catalog.models import Product, Category, Age, Brand, Color
from django.utils.encoding import smart_str
from additions import products_filter


def catalog_view(request):
    products = Product.objects.all()[:40]
    categ = Category()
    categ.name = "Каталог"
    return render_to_response("category.html", {'categ': categ, 'products': products})


def product_view(request, id=-1):
    try:
        product = Product.objects.get(id=id)
        images_mass = product.images.split(";")
        images = []
        for img in images_mass:
            if img != "":
                images.append(img)

        sizes = product.sizes.split(",")

        size_colors = {}
        for st_color in product.size_colors.split(";"):
            if st_color != '':
                cl = st_color.split(":")
                size_colors[cl[0]] = []
                mass_color_id = cl[1].split(",")
                for color_id in mass_color_id:
                    if color_id != '':
                        try:
                            col = Color.objects.get(id=int(color_id))
                            size_colors[cl[0]].append(col)
                        except Color.DoesNotExist:
                            pass

        return render_to_response("product.html", {
            'user': request.user,
            'product': product,
            'images': images,
            'sizes': sizes,
            'sizes_one': sizes[0],
            'colors': product.colors.all(),
            'recommended': product.similar.all(),
            'ages': product.age.all(),
            'size_colors': size_colors,
            'collection': product.collection.all(),
        })
    except Product.DoesNotExist:
        raise Http404


def category_view(request, url="none"):
    try:
        categ = Category.objects.get(url=url)
        products = categ.get_all_product()
        stop_price = 0

        for product in products:
            if product.sale_status and product.price_sale >= stop_price:
                stop_price = product.price_sale
            elif product.price >= stop_price:
                stop_price = product.price

        path = list(reversed(categ.get_path_categ()))
    except Category.DoesNotExist:
        return Http404
    return render_to_response("category.html", {
        'path': path,
        'categ': categ,
        'products': products,
        'stop_price': stop_price,
    })


def category_ajax_view(request):
    products = []
    if request.GET:
        try:
            categ = Category.objects.get(id=request.GET.get('categ', ''))
            products = products_filter({
                'products': categ.get_all_product(),
                'start_price': int(request.GET.get('start_price', '0')),
                'stop_price': int(request.GET.get('stop_price', '0')),
                'collections': request.GET.get('collections', '').split(";"),
            })
        except Category.DoesNotExist:
            pass
    return render_to_response("category_ajax.html", {'products': products})


def age_filter_view(request, id=-1):
    try:
        age = Age.objects.get(id=id)
        products = Product.objects.filter(age=age)
        return render_to_response("category.html", {
            'categ': age,
            'products': products
        })
    except Age.DoesNotExist:
        raise Http404


def brand_filter_view(request, id=-1):
    try:
        brand = Brand.objects.get(id=id)
        products = Product.objects.filter(brand=brand)
        return render_to_response("category.html", {
            'categ': brand,
            'products': products
        })
    except Brand.DoesNotExist:
        raise Http404


def product_edit_afax_related(request):
    key = smart_str(request.GET.get('key'))
    models = Product.objects.filter(name__contains=key)[:7]
    return render_to_response('admin/edit_ajax_related.html', {'models': models, 'key': key})


def product_edit_ajax_research(request, pr_id=-1):
    if pr_id == -1:
        return Http404
    pr = Product.objects.get(id=pr_id)
    return render_to_response("admin/edit_ajax_research.html", {'product': pr})
