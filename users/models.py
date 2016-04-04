from __future__ import unicode_literals

from django.db import models


# Create your models here.
class LogIn(models.Model): 	
    email = models.EmailField()
    password = models.CharField(max_length=50,)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email


class CreateStudent(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	password = models.CharField(max_length=30)
	#timestamp - when user is created
	timestamp = models.DateTimeField(auto_now_add=True)

class Professor(CreateStudent):
	pass

