from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from . import views

urlpatterns = [
	url(r'^state/$', views.index, name='state'),
    url(r'^state/list/$', views.state_list, name='state_list'),
    url(r'^state/add$', views.state_add, name='state_add'),
    url(r'^state/edit/(?P<id>\d+)$', views.state_edit, name='state_edit'),
    url(r'^state/delete/(?P<id>\d+)$', views.state_del, name='state_edit'),
    url(r'^state/city/list/$', views.city_list, name='city_list'),
    url(r'^state/city/add$', views.city_add, name='city_add')
]
