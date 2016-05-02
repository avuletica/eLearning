from __future__ import unicode_literals
import os

from django.db import models
from users.models import UserProfile
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(unique=True, max_length=20)
    course_created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, default=1)
    students = models.ManyToManyField(UserProfile, related_name='students_to_course')
    for_everybody = models.BooleanField(default=True)

    def __unicode__(self):
        return self.course_name


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=20)
    chapter_created_date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.chapter_name

    def get_absolute_url(self):
        return reverse("chapter", kwargs={"course_name": self.course,
                                          "slug": self.slug})

    def slug_default(self):
        slug = create_slug(new_slug=self.chapter_name)
        return slug


def create_slug(instance=None, new_slug=None):
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


class FileUpload(models.Model):
    file = models.FileField(null=False, blank=False, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    file_fk = models.ForeignKey(Chapter, default=1)


@receiver(models.signals.post_delete, sender=FileUpload)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
