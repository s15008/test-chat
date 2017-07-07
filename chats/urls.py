from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<board_id>[0-9]+)/$', views.index, name='index'),
    url(r'^(?P<board_id>[0-9]+)/post$', views.post_message, name='post_message'),
    url(r'^(?P<board_id>[0-9]+)/get$', views.get_message, name='get_message'),
]
