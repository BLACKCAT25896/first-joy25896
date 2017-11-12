from django.conf.urls import url
from django.contrib import admin

from .views import (
    home,
    about,

	)

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^about/$', about),
]