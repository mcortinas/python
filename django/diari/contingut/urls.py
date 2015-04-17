from django.conf.urls import patterns, include, url
from contingut import views

urlpatterns = patterns('',
                       url(r'^cover/$',
                           views.contingut,
                           name='cover'),
                       url(r'^new/([0-9]+)$',
                           views.contingut,
                           name='new'),
                       url(r'^section/([A-Za-z]+)$',
                           views.contingut,
                           name='section'),
                       url(r'^contact/$',
                           views.contingut,
                           name='contact'),
                       )
