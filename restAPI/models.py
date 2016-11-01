from django.db import models
from mongoengine import *

class Tag(Document):
    tag_id = StringField(required=True)
    date_time = DateTimeField(auto_now=True)

class Bagagem(Document):
    documento = StringField(required=True)
    localizacao = StringField(required=True)
    peso = StringField(required=True)
    tag_id = StringField()

class Passageiro(Document):
    nome = StringField(required=True)
    sobrenome = StringField(required=True)
    data_nascimento = DateTimeField(auto_now=False)
    documento = StringField(required=True)
    nacionalidade = StringField(required=True)
    tag_id = StringField()

class Leitura(Document):
    tag_id = StringField(required=True)
    sender_id = StringField(required=True)
    date_time = DateTimeField(auto_now=True)