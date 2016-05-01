# Introduction
E-Learning is scalable web application written in python (django). E-Learning was written with user experience  in
 mind, aiming to solve user transition, so by design it’s an extremely good looking and well polished.

# Installation
Assuming you use virtualenv, follow these steps to download and run the
e-learning application in this directory:

    $ git clone https://github.com/ExtensionEngine/elearning-orange.git
    $ cd elearning-orange
    $ virtualenv venv
    $ source ./venv/bin/activate
    $ pip install -r requirements
    $ python manage.py runserver

Visit http://127.0.0.1:8000/

* Initial data supports 3 types of users for testing purposes:
    * User (username=user, password=letmein123)
    * Professor (username=professor, password=letmein123)
    * Admin (username=admin, password=letmein123)

# Compatibility
* Python 2.7
* Django 1.9
* SQLite, PostgreSQL, MySQL, SQLite

# Notes
* This project uses third-party library tinymce (https://www.tinymce.com/) with own licence
    * Licence is located in static_files/js/tinymce

