from django.db import models
from mongoengine import *

class information(Document):
    tag_id = StringField(required=True)
    sender_id = StringField(required=True)
    date_time = DateTimeField(auto_now=True)