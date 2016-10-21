from django.conf.urls import url
from django.http import HttpResponseRedirect

from . import views

urlpatterns  = [
        url(r'postNewInfo', views.postNewInfo, name="postNewInfo"),
]
