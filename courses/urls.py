from django.conf.urls import url
from . import views as course_views
from users import views as user_views

urlpatterns = [
    url(r'^$', course_views.courses, name='courses'),

    url(r'^(?P<course_name>[\w ]+)/$', user_views.course_homepage, name='course_homepage'),
    url(r'^(?P<course_name>[\w ]+)/(?P<chapter_name>[\w ]+)/$', user_views.student_course,
        name='student_course'),
]
