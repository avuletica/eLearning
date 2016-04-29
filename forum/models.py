from __future__ import unicode_literals

from django.db import models


class Topic(models.Model):
    subject = models.CharField(max_length=20)
    topic_message = models.TextField(max_length=1000)
    author = models.CharField(max_length=30)
    comment_count = models.IntegerField(default=1)
    stamp_created = models.DateTimeField(auto_now_add=True)
    stamp_updated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)


class Comment(models.Model):
    message = models.TextField()
    author = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    comment_fk = models.ForeignKey(Topic)
