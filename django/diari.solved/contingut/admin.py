# -*- coding: utf-8 -*-

from django.contrib import admin
from contingut import models
from django.contrib.admin import SimpleListFilter

class CategoryInline(admin.TabularInline):
    model = models.Category

class CategoryAdminModel(admin.ModelAdmin):
    inlines = [
        CategoryInline
    ]
    exclude = ("slug",)
    class Meta:
        models.Category

class CommentInline(admin.TabularInline):
    model = models.Comment

class ArticleAdminModel(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
    exclude = ("slug",)
    read_only = ("num_visits",)
    class Meta:
        models.Article

class ClientMessageAdminModel(admin.ModelAdmin):
    class Meta:
        models.ClientMessage

class AdAdminModel(admin.ModelAdmin):
    class Meta:
        models.Ad

admin.site.register(models.Category, CategoryAdminModel)
admin.site.register(models.Article, ArticleAdminModel)
admin.site.register(models.Ad, AdAdminModel)
admin.site.register(models.ClientMessage, ClientMessageAdminModel)
