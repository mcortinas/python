from django.conf.urls import patterns, include, url
from contingut import views

urlpatterns = patterns('',
                       url(r'^$',
                           views.main,
                           name='main'),
                       url(r'^categoria/([a-zA-Z0-9\-\_\.]+)$',
                           views.category_detail,
                           name='category_detail'),
                       url(r'^noticia/([a-zA-Z0-9\-\_\.]+)$',
                           views.article_detail,
                           name='article_detail'),
                       url(r'^contact/$',
                           views.contact,
                           name='contact'),
                       )
