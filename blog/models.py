from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=240)
    title_image = models.CharField(max_length=400, default="")
    body_teaser = models.CharField(max_length=400, default="")
    body = models.TextField()
    date = models.DateTimeField()
    posted_by = models.CharField(max_length=100, default="Admin")
