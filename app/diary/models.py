from datetime import datetime
from mongoengine import Document
from mongoengine.fields import StringField, BooleanField, DateTimeField, ReferenceField

from app.accounts.models import Account


class Diary(Document):
    # owner = ReferenceField(Account, reverse_delete_rule=mongoengine.CASCADE)
    title = StringField(min_length=1, max_length=50, required=True)
    body = StringField(max_length=2000)
    creation = DateTimeField(default=datetime.utcnow())
    
    def __str__(self):
        return self.title
