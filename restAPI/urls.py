from django.conf.urls import url
from django.http import HttpResponseRedirect

from . import views

urlpatterns  = [
    url(r'atualizar/localizacao/bagagem$', views.localizacao, name="localizacao"),
    url(r'passageiros/(?P<documento>\w{0,50})/bagagens', views.passageiro_bagagens, name="passageiro_bagagens"),
    url(r'passageiros/(?P<documento>\w{0,50})', views.passageiro, name="passageiro"),
    url(r'tags/(?P<tag_id>\w{0,50})', views.tags_identificacao, name="tags_identificacao"),
    url(r'passageiros', views.passageiros, name="passageiros"),
    url(r'bagagens', views.bagagens, name="bagagens"),
    url(r'tags', views.tags, name="tags"),
    url(r'leituras', views.leituras, name="leituras"),
]
