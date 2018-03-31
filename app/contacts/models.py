from mongoengine import Document
from mongoengine.fields import StringField, BooleanField, DateTimeField, ReferenceField

from app.accounts.models import Account


class Contact(Document):
    owner = ReferenceField(Account, reverse_delete_rule=mongoengine.CASCADE)
    name = StringField(min_length=1, max_length=50, required=True)
    surname = StringField(min_length=1, max_length=50)
    phone = StringField(max_length=50)
    email_address = StringField(max_length=50)
    home_address = StringField(max_length=100)
    birthday = DateTimeField()
    add_reminder = BooleanField(default=False)
    
    def __str__(self):
        return self.name
