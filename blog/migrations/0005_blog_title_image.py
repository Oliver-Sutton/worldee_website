# Generated by Django 2.0.1 on 2018-02-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title_image',
            field=models.CharField(default='', max_length=400),
        ),
    ]
