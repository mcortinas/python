# -*- coding: utf-8 -*-
# Tag to display comments
# Tag to display sidebar with the following content:
## Most visited (by visits)
## Trending topics (by #comments)

from django import template
from contingut import models


register = template.Library()

@register.inclusion_tag('parts/comments.html', takes_context = True)
def show_comments(context):
    instance = context.get("instance")
    comments = models.Comment.objects.get_comments_by_article(instance)
    return {
        'comments': comments
        }

@register.inclusion_tag('parts/menu.html', takes_context = True)
def show_menu(context):
    categories = models.Category.objects.get_parents()
    return {
        'categories': categories
        }

@register.inclusion_tag('parts/sidebar.html', takes_context = True)
def show_sidebar(context):
    return {
        }

@register.inclusion_tag('parts/advertising.html', takes_context = True)
def show_advertising(context):
    ads = models.Ad.objects.all().order_by("?")[0:3]
    return {
        'ads': ads
        }

@register.inclusion_tag('parts/most_visited.html', takes_context = True)
def show_most_visited(context):
    articles = models.Article.objects.get_most_visited()
    return {
        'articles': articles
        }

@register.inclusion_tag('parts/trending_topics.html', takes_context = True)
def show_trending_topics(context):
    articles = models.Article.objects.get_trending_topics()
    return {
        'articles': articles
        }
