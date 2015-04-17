# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

import datetime
from django.utils.timezone import utc

from contingut import managers
# Create your models here.

class Category(models.Model):
    # Relations
    parent = models.ForeignKey("Category",
                               blank = True,
                               null = True,
                               related_name = "children",
                               verbose_name = u"parent")
    # Attributes
    name = models.CharField(max_length = 100,
                            verbose_name = u"name")
    slug = models.SlugField(max_length = 100,
                            verbose_name = u"slug")

    objects = managers.CategoryManager()

    # Functions
    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(args, kwargs)

    class Meta:
        verbose_name = u"Categoria"
        verbose_name_plural = u"Categories"
        ordering = ["id"]

class Article(models.Model):
    # Relations
    category = models.ForeignKey("Category",
                                 related_name = "articles",
                                 verbose_name = u"category")
    # Attributes
    title = models.CharField(max_length = 100,
                             verbose_name = u"title")
    slug = models.SlugField(max_length = 100,
                            verbose_name = u"slug")
    summary = models.TextField(verbose_name = u"summary")
    content = models.TextField(verbose_name = u"content")
    num_visits = models.IntegerField(default = 0,
                                     verbose_name = u"Visites")
    publish_date = models.DateTimeField(blank = True,
                                        null = True,
                                        verbose_name = u"publish date")

    objects = managers.ArticleManager()

    # Functions
    def __unicode__(self):
        return unicode(self.id)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(args, kwargs)

    class Meta:
        verbose_name = u"Article"
        verbose_name_plural = u"Articles"
        ordering = ["-publish_date"]

class Comment(models.Model):
    # Relations
    article = models.ForeignKey("Article",
                                related_name = "comments",
                                verbose_name = u"article")
    # Attributes
    author = models.CharField(max_length = 100,
                              verbose_name = u"author")
    message = models.TextField(verbose_name = u"message")
    timestamp = models.DateTimeField(verbose_name = u"timestamp")

    objects = managers.CommentManager()

    # Functions
    def __unicode__(self):
        return unicode(self.id)

    def save(self, *args, **kwargs):
        if not self.timestamp:
            self.timestamp = datetime.datetime.utcnow().replace(tzinfo = utc)
        super(Comment, self).save(args, kwargs)


    class Meta:
        verbose_name = u"Comentari"
        verbose_name_plural = u"Comentaris"
        ordering = ["id"]

class Ad(models.Model):
    # Relations

    # Attributes
    name = models.CharField(max_length = 100,
                            verbose_name = u"name")
    uri = models.URLField(verbose_name = u"uri")

    # Functions
    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        verbose_name = u"Anunci"
        verbose_name_plural = u"Anuncis"
        ordering = ["id"]

class ClientMessage(models.Model):
    # Relations
    
    # Attributes
    title = models.CharField(max_length = 100,
                             verbose_name = u"title")
    phone = models.CharField(max_length = 50,
                             blank = True,
                             null = True,
                             verbose_name = u"phone")
    mail = models.EmailField(verbose_name = u"mail")
    message = models.TextField(verbose_name = u"message")
    timestamp = models.DateTimeField(verbose_name = u"timestamp")
    # Functions
    def __unicode__(self):
        return unicode(self.id)

    def save(self, *args, **kwargs):
        if not self.timestamp:
            self.timestamp = datetime.datetime.utcnow().replace(tzinfo = utc)
        super(ClientMessage, self).save(args, kwargs)

    class Meta:
        verbose_name = u"Missatge client"
        verbose_name_plural = u"Missatges client"
        ordering = ["-timestamp"]
    
