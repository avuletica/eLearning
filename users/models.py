from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    is_professor = models.BooleanField(default=False)
    is_site_admin = models.BooleanField(default=False)
