from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProxy(User):
    class Meta:
        proxy = True


class DeleteUser(models.Model):
    username = models.CharField(max_length=30)
