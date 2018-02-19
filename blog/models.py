from django.db import models

# Create your models here.

BLOG_CHOICES = (
    ('TRAVEL', 'Travel'),
    ('ATTRACTIONS', 'Attractions'),
    ('FOOD', 'Food')
)

class Blog(models.Model):
    title = models.CharField(max_length=240)
    title_image = models.CharField(max_length=400, default="")
    type = models.CharField(max_length=50, choices=BLOG_CHOICES, default="")
    body_teaser = models.CharField(max_length=400, default="")
    body = models.TextField()
    date = models.DateTimeField()
    posted_by = models.CharField(max_length=100, default="Admin")

class TopPosts(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
