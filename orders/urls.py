from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'orders.views.orders_view'),
    url(r'^create/$', 'orders.views.create_order'),
    url(r'^thanks/$', 'orders.views.thank_order'),
    url(r'^reg_thanks/$', 'orders.views.reg_thank_order'),
)
