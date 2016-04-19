from django.conf.urls import url
from . import views as course_views

urlpatterns = [
    url(r'^$', course_views.courses, name='courses'),

    url(r'^(?P<course_name>[\w ]+)/$', course_views.course, name='course'),
    url(r'^(?P<course_name>[\w ]+)/delete/$', course_views.delete_course, name='delete'),
    url(r'^(?P<course_name>[\w ]+)/(?P<chapter_name>[\w ]+)/$', course_views.chapter, name='chapter'),
    url(r'^(?P<course_name>[\w ]+)/(?P<chapter_id>[\d ]+)/delete/$', course_views.delete_chapter, name='delete_chapter'),
    url(r'^(?P<course_name>[\w ]+)/(?P<chapter_name>[\w ]+)/(?P<txt_id>[\d ]+)/delete/$', course_views.delete_text_block, name='delete_txt'),
    url(r'^(?P<course_name>[\w ]+)/(?P<chapter_name>[\w ]+)/delete/(?P<yt_id>[\d ]+)/$', course_views.delete_yt_link, name='delete_link'),
]
