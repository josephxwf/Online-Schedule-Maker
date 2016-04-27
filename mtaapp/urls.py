from django.conf.urls import patterns, include, url

from . import views
from django.contrib import admin


admin.autodiscover()

urlpatterns = [

    url(r'^$', views.index),

    #url(r'^calendar/$', views.calendar,name='calendars'),
    #url(r'^register/$', views.register,name='register'),
    url(r'^login/$', views.login_page,name='login_page'),
    url(r'^login2/$', views.nextQuarter,name='login_page2'),
    url(r'^invalid_login/$', views.invalid_login,name='invalid_login'),
    #url(r'^loggedin/$', views.loggedin,name='loggedin'),
    url(r'^auth/$', views.auth_view,name='auth'),
    url(r'^auth2/$', views.auth_viewSecond,name='auth2'),
    url(r'^logout/$', views.logout_page,name='logout_page'),



]
