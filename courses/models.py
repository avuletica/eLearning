from __future__ import unicode_literals

from django.db import models
from users.models import User


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    course_link = models.CharField(max_length=50)
    user_fk = models.ManyToManyField(User)


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    course_fk = models.ForeignKey(Course)


class TextBlock(models.Model):
    chapter_description = models.TextField(max_length=2048, default='')
    text_area_fk = models.ForeignKey(Chapter)


class YTLink(models.Model):
    link = models.URLField(max_length=200, default='')
    youtube_fk = models.ForeignKey(Chapter)
