from django.conf.urls import url
from . import views as course_views

urlpatterns = [
    url(r'^$', course_views.courses, name='courses'),
    url(r'^(?P<course_name>\w+)', course_views.course, name='course'),
]