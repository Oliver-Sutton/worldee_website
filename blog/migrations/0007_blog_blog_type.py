# Generated by Django 2.0.1 on 2018-02-01 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_body_teaser'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_type',
            field=models.CharField(default='', max_length=50),
        ),
    ]
