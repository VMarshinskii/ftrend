from django.contrib import admin
from models import Sale


class SaleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}

admin.site.register(Sale, SaleAdmin)
