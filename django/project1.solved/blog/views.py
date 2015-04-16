# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from blog import models

def blog(request):
    posts = models.Post.objects.all()
    outstanding_posts = models.Post.objects.all().order_by("-visits")[0:3]
    return render_to_response("public/blog.html",
                              RequestContext(request,
                                             {
                                                 'posts': posts,
                                                 'outstanding_posts': outstanding_posts
                                                 }
                                             )
                              )

def post(request, post_id):
    post = models.Post.objects.prefetch_related("links").get(id = post_id)
    links = post.links.all()
    post.visits += 1
    post.save()
    outstanding_posts = models.Post.objects.all().order_by("-visits")[0:3]
    return render_to_response("public/post.html",
                              RequestContext(request,
                                             {
                                                 'post': post,
                                                 'links': links,
                                                 'outstanding_posts': outstanding_posts
                                                 }
                                             )
                              )
