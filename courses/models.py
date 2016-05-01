from __future__ import unicode_literals

from django.db import models
from users.models import UserProfile
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

from django.utils.text import slugify


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(unique=True, max_length=50)
    course_created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, default=1)
    students = models.ManyToManyField(UserProfile, related_name='students_to_course')

    def __unicode__(self):
        return self.course_name


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=50)
    chapter_created_date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(unique=True, default='')

    def __unicode__(self):
        return self.chapter_name

    def get_absolute_url(self):
        return reverse("chapter", kwargs={"course_name": self.course,
                                          "slug": self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.chapter_name)

    if new_slug is not None:
        slug = new_slug

    qs = Chapter.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)

    return slug


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_receiver, sender=Chapter)


class TextBlock(models.Model):
    lesson = models.TextField()
    text_block_fk = models.ForeignKey(Chapter, default=1)
    date_created = models.DateTimeField(auto_now_add=True)


class YTLink(models.Model):
    link = models.URLField(max_length=200)
    yt_link_fk = models.ForeignKey(Chapter, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
