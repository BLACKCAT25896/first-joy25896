from django.conf.urls import url
from django.contrib import admin

from .views import (
    home,
    home1,
    about,

	)

urlpatterns = [
	url(r'^home$', home, name='home'),
    url(r'^$', home1, name='home1'),
    url(r'^about/$', about),
]