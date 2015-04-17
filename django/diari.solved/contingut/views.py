# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from contingut import models
from contingut import forms

def category_detail(request, category_slug):
    """
    This view displays a list of articles, sorted by latest, from desired category
    """
    category = models.Category.objects.get(slug = category_slug)
    categories = category.children.all()
    articles = models.Article.objects.get_by_category(category)
    return render_to_response("public/category_detail.html",
                              RequestContext(request,
                                             {
                                                 'categories': categories,
                                                 'category': category,
                                                 'articles': articles
                                                 }
                                             )
                              )

def main(request):
    """
    This view displays the main page, consisting in a paginated article list, ordering by latests.
    """
    articles = models.Article.objects.get_published()[0:10]
    return render_to_response("public/main.html",
                              RequestContext(request,
                                             {
                                                 'articles': articles
                                                 }
                                             )
                              )

def article_detail(request, article_slug):
    """
    This view displays all content from selected article
    """
    article = models.Article.objects.get(slug = article_slug)
    article.num_visits += 1
    article.save()
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.article = article
            instance.save()
            form = forms.CommentForm()
    else:
        form = forms.CommentForm()
    return render_to_response("public/article_detail.html",
                              RequestContext(request,
                                             {
                                                 'instance': article,
                                                 'form': form
                                                 }
                                             )
                              )

def contact(request):
    """
    This view shows the contact form and stores all needed information about this message
    """
    message = ""
    if request.method == "POST":
        form = forms.ClientMessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.ClientMessageForm()
            message = "Missatge enviat correctament"
    else:
        form = forms.ClientMessageForm()
    return render_to_response("public/contact.html",
                              RequestContext(request,
                                             {
                                                 'form': form,
                                                 'message': message
                                                 }
                                             )
                              )
