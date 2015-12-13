from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'sale.views.sales_view'),
    url(r'^(?P<url>[\-\w]+)/$', 'sale.views.sale_view'),
)
