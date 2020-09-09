from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'tablets'

urlpatterns = [
    url(r'^create/$', views.tablet_create, name='create'),
    url(r'^(?P<pk>[\w-]+)/$', views.tablet_detail, name='detail'),
    url(r'^edit/(?P<pk>\d+)/$', views.tablet_update, {}, 'tablet_update'),
    url(r'^delete_tablet/(?P<pk>\d+)/$', views.delete_tablet, name='delete'),
]