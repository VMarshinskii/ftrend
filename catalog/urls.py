from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'catalog.views.catalog_view'),
    url(r'^novelty/$', 'catalog.views.novelty_view'),
    url(r'^popular/$', 'catalog.views.popular_view'),
    url(r'^sell/$', 'catalog.views.sell_view'),
    url(r'^product/(?P<id>\d+)/$', 'catalog.views.product_view'),
    url(r'^age/(?P<url>[\-\w]+)/$', 'catalog.views.age_filter_view'),
    url(r'^brand/(?P<url>[\-\w]+)/$', 'catalog.views.brand_filter_view'),
    url(r'^filter/$', 'catalog.views.category_ajax_view'),
    url(r'^(?P<url>[\-\w]+)/$', 'catalog.views.category_view')
)
