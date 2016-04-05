from __future__ import unicode_literals

from django.db import models
from users.models import User

# Create your models here.
class Course(models.Model):
	course_name = models.CharField(max_length=50)
	created_date = models.DateTimeField(auto_now_add=True)
	professor_fk = models.ForeignKey(User) # verify
	free_course = models.BooleanField(default='True') #free or not free


class Chapter(models.Model):
	chapter_name = models.CharField(max_length=50)
	created_date = models.DateTimeField(auto_now_add=True)
	course_fk = models.ForeignKey(Course)

class TeachingBlock(models.Model):
	link = models.URLField(max_length=200, default='Insert your YouTube video link here')
	chapter_description = models.TextField(max_length=2048, default='Write your course description here')
	chapter_fk = models.ForeignKey(Chapter)	
	