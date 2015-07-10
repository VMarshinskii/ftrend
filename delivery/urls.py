from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^list_cdek/$', 'delivery.views.points_sdk_view'),
)
