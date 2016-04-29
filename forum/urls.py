from django.conf.urls import url
from . import views as forum_views

urlpatterns = [
    url(r'^$', forum_views.forum, name='forum'),
    url(r'^(?P<slug>[\w-]+)/$', forum_views.topic, name='topic'),
]
