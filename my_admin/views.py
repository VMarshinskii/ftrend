# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse, Http404, redirect
from django.template.context_processors import csrf
from django.utils.encoding import smart_str
from ftrend.additions import upload_file
from catalog.models import Color, Category
from models import Settings


def video_upload(request):
    if request.method == 'POST' and request.user.is_authenticated():
        f = request.FILES['file']
        path = "/static/uploads/"
        url = upload_file(f, path)
        return HttpResponse(url)
    return HttpResponse("no")


def size_colors(request, data):
    if request.user.is_authenticated():
        selected_colors = data.split(",")
        colors = []
        for color in Color.objects.all():
            if str(color.id) in selected_colors:
                color.selected = 'selected="selected"'
            colors.append(color)
        return render_to_response("size_colors.html", {'colors': colors})
    return HttpResponse("False")


def sort_list():
    mass_object = []
    roots = Category.objects.filter(parent=None)

    def rec_list(obj):
        obj.title = smart_str("— "*obj.step) + smart_str(obj.title)
        mass_object.append(obj)
        children = Category.objects.filter(parent=obj)

        for child in children:
            rec_list(child)

    for root in roots:
        rec_list(root)

    return mass_object


def tree_categories(request, id=-1):
    if request.user.is_authenticated():
        return render_to_response("tree_categories.html", {
            'categories': sort_list(),
        })
    raise Http404


def settings(request):
    if request.user.is_authenticated():
        model = Settings.objects.get(id=1)
        args = {}
        if request.POST:
            model.title = request.POST.get('title')
            model.email = request.POST.get('email')
            model.description = request.POST.get('description')
            model.phone_home = request.POST.get('phone')
            model.contacts = request.POST.get('contacts')
            model.delivery = request.POST.get('delivery')
            model.pay = request.POST.get('pay')
            model.recovery = request.POST.get('recovery')
            model.terms = request.POST.get('terms')
            model.footer_link = request.POST.get('footer_link')
            model.save()
            args['message'] = "yes"
        args.update(csrf(request))
        args['model'] = model
        return render_to_response("set.html", args)
    else:
        return redirect('/admin/')