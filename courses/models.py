from __future__ import unicode_literals

from django.db import models
from users.models import Professor

# Create your models here.
class Course(models.Model):
	course_name = models.CharField(max_length=50)
	created_date = models.DateTimeField(auto_now_add=True)
	professor = models.ForeignKey(Professor)


class Chapter(models.Model):
	chapter_name = models.CharField(max_length=50)
	created_date = models.DateTimeField(auto_now_add=True)
	course = models.ForeignKey(Course)