# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

import datetime
from django.utils.timezone import utc

class New(models.Model):
    title = models.CharField(max_length = 300, verbose_name = u"title")
    short_body = models.TextField(verbose_name = u"short body")
    body = models.TextField(verbose_name = u"body")
    created_at = models.DateTimeField(verbose_name = u"created at")
    published_at = models.DateTimeField(verbose_name = u"published at")
    visits = models.IntegerField(default = 0, verbose_name = u"visits")
    # Relations
    section = models.ForeignKey(u"Section",
                             related_name = u"links",
                             verbose_name = u"section")
    # Functions
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ("section", [str(self.id)])

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.utcnow().replace(tzinfo = utc)
        super(Post, self).save(args, kwargs)

    class Meta:
        ordering = ["-published_at"] 
    
class Announce(models.Model):
    title = models.CharField(max_length = 300, verbose_name = u"title")
    body = models.TextField(verbose_name = u"body")

class Section(models.Model):
    title = models.CharField(max_length = 300,
                             verbose_name = u"title")
    description = models.TextField(verbose_name = u"description")
    
    # Relations
    section = models.ForeignKey(u"Section",
                             related_name = u"links",
                             verbose_name = u"section")