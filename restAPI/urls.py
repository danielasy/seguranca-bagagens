from django.conf.urls import url
from django.http import HttpResponseRedirect

from . import views

urlpatterns  = [
    url(r'passageiros$', views.passageiros, name="passageiros"),
    url(r'atualizar/localizacao/bagagem$', views.localizacao, name="localizacao"),
    url(r'passageiros/(?P<documento>\w{0,50})/bagagens', views.bagagens, name="bagagens"),
]
