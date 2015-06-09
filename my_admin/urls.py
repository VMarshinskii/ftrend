from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^upload_image/$', 'my_admin.views.video_upload'),
    url(r'^size_colors/(?P<data>[\-,\w]+)/$', 'my_admin.views.size_colors'),
    url(r'^tree_categories/(?P<id>\d+)/', 'my_admin.views.tree_categories'),
)
