from django import template
from catalog.models import Category, Age, Brand
register = template.Library()


@register.inclusion_tag('../templates/top_menu_tag.html')
def top_menu():
    categories = Category.objects.filter(parent=None)
    age_girls = Age.objects.filter(type='girls')
    age_boys = Age.objects.filter(type='boys')
    brands = Brand.objects.all()
    return {
        'categories': categories,
        'age_girls': age_girls,
        'age_boys': age_boys,
        'brands': brands,
    }
