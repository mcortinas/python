from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
                       url(r'^blog/$',
                           views.blog,
                           name='blog'),
                       url(r'^post/([0-9]+)$',
                           views.post,
                           name='post'),
                       )
