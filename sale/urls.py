from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^(?P<url>[\-\w]+)/$', 'sale.views.sale_view'),
)
