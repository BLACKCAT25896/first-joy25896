from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^enter/$', views.Enter, name='enter'),
    url(r'^logout/$', views.Logout, name='logout'),
    # url(r'^home/$', views.Home, name='home'),
    url(r'^bal/$', views.Bal, name='bal'),
    url(r'^post/$', views.Post, name='post'),
    url(r'^messages/$', views.Messages, name='messages'),
]