from __future__ import unicode_literals
from django.db import models, migrations

from django.contrib.auth.hashers import make_password


def initial_users(apps, schema_editor):
    user = apps.get_model("users", "UserProfile")

    user(username='user',
         email='username.one@gmail.com',
         password=make_password('letmein123'),
         ).save()

    user(username='professor',
         email='username.two@gmail.com',
         password=make_password('letmein123'),
         is_professor=True,
         ).save()

    user(username='admin',
         email='username.three@gmail.com',
         password=make_password('letmein123'),
         is_site_admin=True,
         ).save()

    user(username='test',
         email='username.test@gmail.com',
         password=make_password('letmein123'),
         ).save()

    user(username='test2',
         email='username.test2@gmail.com',
         password=make_password('letmein123'),
         ).save()

    user(username='test3',
         email='username.test3@gmail.com',
         password=make_password('letmein123'),
         ).save()

    user(username='test4',
         email='username.test4@gmail.com',
         password=make_password('letmein123'),
         ).save()

    user(username='test5',
         email='username.test5@gmail.com',
         password=make_password('letmein123'),
         ).save()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_users)
    ]
