from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'sale.views.index_view'),
    url(r'^login/$', 'account.views.login'),
    url(r'^logout/$', 'account.views.logout'),
   url(r'^authentication/$', 'account.views.authentication'),
    url(r'^registration/$', 'account.views.registration'),
    url(r'^admin/', include('my_admin.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^orders/', include('orders.urls')),
    url(r'^sale/', include('sale.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^robokassa/', include('robokassa.urls')),
    url(r'^(?P<url>[\-\w]+)', 'pages.views.page_view'),
)