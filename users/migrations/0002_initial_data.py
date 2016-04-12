from __future__ import unicode_literals
from django.db import models, migrations

from django.contrib.auth.hashers import make_password

def initial_users(apps, schema_editor):
	UserProxy = apps.get_model("users", "UserProxy")

	UserProxy(username = 'UserNameOne',
		email = 'username.one@gmail.com',
		password = make_password('letmein123')
		).save()

	UserProxy(username = 'UserNameTwo',
		email = 'username.two@gmail.com',
		password = make_password('letmein1234')
		).save()

class Migration(migrations.Migration):

	dependencies = [
		('users', '0001_initial'),
	]

	operations = [
		migrations.RunPython(initial_users)
	]