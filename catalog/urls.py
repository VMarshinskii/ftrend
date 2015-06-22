from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'catalog.views.catalog_view'),
    url(r'^product/(?P<id>\d+)/$', 'catalog.views.product_view'),
    url(r'^age/(?P<id>\d+)/$', 'catalog.views.age_filter_view'),
    url(r'^brand/(?P<id>\d+)/$', 'catalog.views.brand_filter_view'),
    url(r'^filter/$', 'catalog.views.category_ajax_view'),
    url(r'^(?P<url>[\-\w]+)/$', 'catalog.views.category_view')
)
