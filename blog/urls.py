from django.urls import path
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import Blog
from . import views

urlpatterns = [
    path('', ListView.as_view(queryset=Blog.objects.all().order_by("-date"),
                            template_name="blog/travel.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Blog, template_name="blog/travel-template.html")),
    path('get_more_posts', views.get_more_posts)

]
