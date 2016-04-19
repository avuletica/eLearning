from django.conf.urls import url
from . import views as user_views

urlpatterns = [
    url(r'^$', user_views.profile, name='profile'),
    url(r'^edit/(?P<username>[\w.@+-]+)', user_views.update_user, name='update_user'),
    url(r'^delete/(?P<username>[\w.@+-]+)', user_views.delete_user, name='delete_user'),
]
