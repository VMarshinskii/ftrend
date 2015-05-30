from django.contrib import admin
from models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'status', 'date_now')


admin.site.register(Order, OrderAdmin)
