from __future__ import unicode_literals

from django.db import models



# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	password = models.CharField(max_length=30)
	#timestamp - when user is created
	timestamp = models.DateTimeField(auto_now_add=True)
	privilege = models.BooleanField(default=False)


