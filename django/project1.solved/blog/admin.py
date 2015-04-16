# -*- coding: utf-8 -*-
from blog import models
from django.contrib import admin
from django.conf import settings

class LinkInline(admin.TabularInline):
        extra = 0
        model = models.Link

class PostAdminModel(admin.ModelAdmin):
    inlines = [
            LinkInline
            ]
    list_display = ("title", "created_at", "published_at", "visits")
    list_filter = ("published_at",)
    search_fields = ["title"]

    class Meta:
        model = models.Post

admin.site.register(models.Post, PostAdminModel)
