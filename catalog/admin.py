# -*- coding: utf-8 -*-
from django.contrib import admin
from catalog.models import Product, Category, Color, Age, Brand, Collection
from django.shortcuts import render_to_response
from django.utils.encoding import smart_str


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}

    def changelist_view(self, request, extra_context=None):
        list_category = sort_list()
        select_res(list_category)
        vars = {'categories': list_category}
        html = render_to_response('admin/result_content_list.html', vars).content
        mass = {'result_content': html}
        return super(CategoryAdmin, self).changelist_view(request, extra_context=mass)


def sort_list():
    mass_object = []
    roots = Category.objects.filter(parent=None)

    def rec_list(obj):
        obj.title = smart_str("— "*obj.step) + smart_str(obj.title)
        mass_object.append(obj)
        children = Category.objects.filter(parent=obj)
        print("sdsd")

        for child in children:
            rec_list(child)

    for root in roots:
        rec_list(root)

    return mass_object


def select_res(categoryes):
    str_res = ""
    for category in categoryes:
        str_res += smart_str(category.title) + ":" + smart_str(category.id) + ";"
    return str_res



class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_prew', 'name', 'code', 'category', 'brand')
    search_fields = ['name', 'category']


admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Age)
admin.site.register(Brand)
admin.site.register(Collection)
admin.site.register(Category, CategoryAdmin)