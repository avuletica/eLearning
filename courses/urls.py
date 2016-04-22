from django.conf.urls import url
from . import views as course_views

urlpatterns = [
    url(r'^$', course_views.courses, name='courses'),

    url(r'^(?P<course_name>[\w ]+)/$', course_views.course, name='course'),
    url(r'^(?P<course_name>[\w ]+)/delete/$', course_views.delete_course, name='delete'),
    url(r'^(?P<course_name>[\w ]+)/edit/$', course_views.update_course, name='edit'),

    url(r'^(?P<course_name>[\w ]+)/students/$', course_views.list_students, name='list_students'),
    url(r'^(?P<course_name>[\w ]+)/students/(?P<student_id>[\d ]+)/remove/$',
        course_views.remove_students, name='remove_students'),
    url(r'^(?P<course_name>[\w ]+)/students/(?P<student_id>[\d ]+)/add/$',
        course_views.add_students, name='add_students'),

    url(r'^(?P<course_name>[\w ]+)/(?P<chapter_name>[\w ]+)/$', course_views.chapter, name='chapter'),
    url(r'^edit/(?P<course_name>[\w ]+)/(?P<chapter_id>[\d ]+)/$',
        course_views.update_chapter, name='edit_chapter'),
    url(r'^delete/(?P<course_name>[\w ]+)/(?P<chapter_id>[\d ]+)/$',
        course_views.delete_chapter, name='delete_chapter'),

    url(r'^(?P<course_name>[\w ]+)/(?P<chapter_id>[\d ]+)/txt/edit/(?P<txt_id>[\d ]+)/$',
        course_views.update_text_block, name='edit_txt'),
    url(r'^txt/delete/(?P<txt_id>[\d ]+)/$', course_views.delete_text_block, name='delete_txt'),

    url(r'^(?P<course_name>[\w ]+)/(?P<chapter_id>[\d ]+)/link/edit/(?P<yt_id>[\d ]+)/$',
        course_views.update_yt_link, name='edit_link'),
    url(r'^link/delete/(?P<yt_id>[\d ]+)/$', course_views.delete_yt_link, name='delete_link'),
]
