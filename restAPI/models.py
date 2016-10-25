from django.db import models
from mongoengine import *

class Passenger(Document):
	nome = StringField(required=True)
	sobrenome = StringField(required=True)
	data_nascimento = DateTimeField(auto_now=False)
	documento = StringField(required=True)
	nacionalidade = StringField(required=True)
	tag = ListField(EmbeddedDocumentField(Tag))
	bagagens = ListField(EmbeddedDocumentField(Bagagem))

class Bagagem(EmbeddedDocument):
	documento = StringField(required=True)
	peso = StringField(required=True)
	tag = ListField(EmbeddedDocumentField(Tag))

class Tag(EmbeddedDocument):
    tag_id = StringField(required=True)
    date_time = DateTimeField(auto_now=True)

class Leitura(Document):
	tag_id = StringField(required=True)
    sender_id = StringField(required=True)
    date_time = DateTimeField(auto_now=True)