from django.conf.urls import url
from django.http import HttpResponseRedirect

from . import views

urlpatterns  = [
    url(r'administrador', views.administrador, name="administrador"),
    url(r'$', views.index, name="index"),
]
