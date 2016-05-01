from django.conf.urls import url
from . import views as user_views
from courses import views as course_views

urlpatterns = [
    url(r'^$', user_views.profile, name='profile'),
    url(r'^student/$', user_views.student, name='student'),

    url(r'^professor/$', user_views.professor, name='professor'),
    url(r'^professor/(?P<course_name>[\w ]+)/$', course_views.course, name='professor_course'),
    url(r'^professor/(?P<course_name>[\w ]+)/delete/$', course_views.delete_course, name='delete'),
    url(r'^professor/(?P<course_name>[\w ]+)/edit/$', course_views.update_course, name='edit'),

    url(r'^professor/(?P<course_name>[\w ]+)/students/$', course_views.list_students, name='list_students'),
    url(r'^professor/(?P<course_name>[\w ]+)/students/(?P<student_id>[\d ]+)/remove/$',
        course_views.remove_students, name='remove_students'),
    url(r'^professor/(?P<course_name>[\w ]+)/students/(?P<student_id>[\d ]+)/add/$',
        course_views.add_students, name='add_students'),

    url(r'^professor/(?P<course_name>[\w ]+)/(?P<slug>[\w-]+)/$', course_views.chapter, name='chapter'),
    url(r'^professor/edit/(?P<course_name>[\w ]+)/(?P<slug>[\w-]+)/$',
        course_views.update_chapter, name='edit_chapter'),
    url(r'^professor/delete/(?P<course_name>[\w ]+)/(?P<slug>[\w-]+)/$',
        course_views.delete_chapter, name='delete_chapter'),

    url(r'^professor/(?P<course_name>[\w ]+)/(?P<slug>[\w-]+)/txt/edit/(?P<txt_id>[\d ]+)/$',
        course_views.update_text_block, name='edit_txt'),
    url(r'^professor/txt/delete/(?P<txt_id>[\d ]+)/$', course_views.delete_text_block, name='delete_txt'),

    url(r'^professor/(?P<course_name>[\w ]+)/(?P<slug>[\w-]+)/link/edit/(?P<yt_id>[\d ]+)/$',
        course_views.update_yt_link, name='edit_link'),
    url(r'^professor/link/delete/(?P<yt_id>[\d ]+)/$', course_views.delete_yt_link, name='delete_link'),

    url(r'^admin/$', user_views.admin, name='admin'),
    url(r'^edit/(?P<username>[\w ]+)/$', user_views.update_user, name='update_user'),
    url(r'^delete/(?P<username>[\w ]+)/$', user_views.delete_user, name='delete_user'),
]
