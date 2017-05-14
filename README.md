# Introduction
Project was created by participating team in extension engine spring camp.
E-Learning is scalable web application written in python (django).
E-Learning was designed to provide pleasant experience for users.
<img src="https://github.com/Bcoolie/eLearning/blob/master/users/static_in_users/static_files/img/home-sample.png" width="720" height="400">
# Installation
Assuming you use virtualenv, follow these steps to download and run the
e-learning application in this directory:

    $ git clone https://github.com/avuletica/eLearning.git
    $ cd eLearning
    $ virtualenv venv
    $ source ./venv/bin/activate
    $ pip install -r requirements
    $ python manage.py migrate
    $ python manage.py runserver

* Initial data supports 3 types of users for testing purposes:
    * User (username=user, password=letmein123)
    * Professor (username=professor, password=letmein123)
    * Admin (username=admin, password=letmein123)
    * Visit http://127.0.0.1:8000/

# Compatibility
* Python 2.7
* Django 1.9
* SQLite, PostgreSQL, MySQL

# Notes
* This project uses third-party library tinymce (https://www.tinymce.com/) with own licence
    * Licence is located in static_files/js/tinymce
* If you wish to use contact/registration features you will need to add settings_sensitive file in source
*	You can find template for settings sensitive in source directory
*	For more information visit (https://docs.djangoproject.com/ja/1.9/topics/email/)
