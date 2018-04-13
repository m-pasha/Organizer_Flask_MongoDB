from datetime import datetime
from mongoengine import Document
from mongoengine.fields import StringField, BooleanField, DateTimeField, ReferenceField

from app.accounts.models import Account


class CategoryTask(Document):
    # owner = ReferenceField(Account, reverse_delete_rule=mongoengine.CASCADE)
    title = StringField(min_length=1, max_length=50, required=True)

    def __str__(self):
        return self.title


class Task(Document):
    # owner = ReferenceField(Account, reverse_delete_rule=mongoengine.CASCADE)
    title = StringField(min_length=1, max_length=250, required=True)
    category = ReferenceField(CategoryTask)
    body = StringField(max_length=500, blank=True, null=True)
    creation = DateTimeField(default=datetime.utcnow())
    start_date = DateTimeField(default=datetime.utcnow())
    finish_date = DateTimeField(default=datetime.utcnow())
    finished = BooleanField(default=False)
    reminder = BooleanField(default=False)
    reminder_date = DateTimeField(default=datetime.utcnow())

    def __str__(self):
        return self.title
