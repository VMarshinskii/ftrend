from django import template
from catalog.models import Category
register = template.Library()


@register.inclusion_tag('catalog_menu_tag.html')
def catalog_menu():
    categories = []

    for categ in Category.objects.filter(parent=None):
        new_cat = categ
        new_cat.childs = Category.objects.filter(parent=categ)
        categories.append(new_cat)

    return {'categories': categories}
