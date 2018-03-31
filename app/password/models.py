from mongoengine import Document
from mongoengine.fields import StringField, ReferenceField

from app.accounts.models import Account


class Password(Document):
    owner = ReferenceField(Account, reverse_delete_rule=mongoengine.CASCADE)
    resource_url = StringField(min_length=1, max_length=100)
    password_res = StringField(min_length=1, max_length=100)
    
    def __str__(self):
        return self.resource_url
