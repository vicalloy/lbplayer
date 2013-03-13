#!/usr/bin/python  
#encoding=utf-8  
from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    url(r'^$', views.player, name="lbplayer_player"),
    url(r'^upload/$', views.upload, name="lbplayer_upload"),
    url(r'^sel_media/$', views.sel_media, name="lbplayer_sel_media"),
    url(r'^ajax/childs/$', views.ajax_childs, name="lbplayer_ajax_childs"),
    url(r'^ajax/medias/$', views.ajax_medias, name="lbplayer_ajax_medias"),
)
