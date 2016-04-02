from __future__ import unicode_literals

from django.db import models


# Create your models here.
class LogIn(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50,)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):  # Python 3.3 is __str__
        return self.email
