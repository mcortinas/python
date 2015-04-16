# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import utc
import datetime

class Post(models.Model):

	#Relations

	#Attributes
	title = models.CharField(max_lenght = 300 ,
				verbose_name = u"title")
	short_body = models.TextField(verbose_name = u"short body")
	body = models.TextField(verbose_name = u"body" )
	created_at = models.DateTimeField(verbose_name = u"created at")
	published_at = models.DateTimeField(verbose_name = u"published at")
	visits = models.IntegerField ( default = 0,
					verbose_name = u"visits")

	#Functions
	def __unicode__(self):
		return self.title

	@models.permlink
	def get_absolute_url(self):
		return ("post", [ str(self.id)])

	def save(self, *args, **kwargs):
		if not self.created_at:
			self.created_at = datetime.datetime.utcnow().replace(tzinfo = utc)
		super(Post, self).save(args, kwargs)

	class Meta:
		ordering = [ "-published_at" ]

	class Link(model.Model):
		#Relations
		post = models.Foreignkey(u"Post",
					related_name = u"links",
					verbose_name = u"post"		
