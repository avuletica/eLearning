from django.conf.urls import url
from . import views as course_views

urlpatterns = [
    url(r'^$', course_views.courses, name='courses'),
    url(r'^(?P<course_name>\w+)/$', course_views.course, name='course'),
    url(r'^(?P<course_name>\w+)/(?P<chapter_name>\w+)/$', course_views.chapter, name='chapter'),
    url(r'^(?P<course_name>\w+)/(?P<chapter_id>\d+)/delete/$', course_views.delete_chapter, name='delete_chapter'),
]