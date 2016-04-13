from __future__ import unicode_literals
from django.db import models, migrations

from django.contrib.auth.hashers import make_password


def initial_users(apps, schema_editor):
    UserProxy = apps.get_model("users", "UserProxy")

    UserProxy(username='user',
              email='username.one@gmail.com',
              password=make_password('letmein123')
              ).save()

    UserProxy(username='staffuser',
              email='username.two@gmail.com',
              password=make_password('letmein123'),
              is_staff=True,
              ).save()

    UserProxy(username='superuser',
              email='username.three@gmail.com',
              password=make_password('letmein123'),
              is_staff=True,
              is_superuser=True,
              ).save()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_users)
    ]
