from django.db import models

# Create your models here.

class FAQDatabase(models.Model):
    question = models.CharField(max_length=140)
    answer = models.CharField(max_length=240)

class NewsLetter(models.Model):
    email = models.CharField(max_length=140)
