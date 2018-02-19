from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog, TopPosts
import json

# Create your views here.

def get_more_posts(request):
    if request.method == 'GET':

        blogs = Blog.objects.order_by('date')[:5]
        data = {}
        for blog in blogs:
            data[blog.id] = json.dumps({ "title": blog.title, "id": blog.id});

        return HttpResponse(json.dumps(data))

    return HttpResponse('')

def get_top_posts(request):
    if request.method == 'GET':

        posts = TopPosts.objects.order_by('date')[:3]
        data = {}
        for post in posts:
            data[post.post.id] = json.dumps({"id": post.post.id, "img": post.post.title_img})

        return HttpResponse(json.dumps(data))

    return HttpResponse('')
