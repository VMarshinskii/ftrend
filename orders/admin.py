from django.contrib import admin
from models import Order, DeliveryType


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'status', 'date_now', 'products.name')


admin.site.register(Order, OrderAdmin)
admin.site.register(DeliveryType)