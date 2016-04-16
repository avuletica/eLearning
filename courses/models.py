from __future__ import unicode_literals

from django.db import models
from users.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(unique=True, max_length=50)
    course_created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse("course", kwargs={"course_name": self.course_name})


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=50)
    chapter_created_date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)

    def __unicode__(self):
        return self.chapter_name

    def get_absolute_url(self):
        return reverse("chapter", kwargs={"course_name": self.course,
                                          "chapter_name": self.chapter_name})


class TextBlock(models.Model):
    chapter_description = models.TextField()
    text_block_fk = models.ForeignKey(Chapter, default=1)


class YTLink(models.Model):
    link = models.URLField(max_length=200, default='')
    yt_link_fk = models.ForeignKey(Chapter, default=1)

