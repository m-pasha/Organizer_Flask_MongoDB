from datetime import datetime
from mongoengine import Document
from mongoengine.fields import StringField, BooleanField, DateTimeField, ReferenceField

from app.accounts.models import Account


class Task(Document):
    owner = ReferenceField(Account)
    title = StringField(min_length=1, max_length=250, required=True)
    body = StringField(max_length=500, blank=True, null=True)
    creation = DateTimeField(default=datetime.utcnow())
    finished = BooleanField(default=False)

    def __str__(self):
        return self.title

    # def crete_task(self, **kwargs):
    #     new_task = Task.objects(title=kwargs['title'],
    #                             body=kwargs['body'],
    #                             creation=kwargs['creation'],
    #                             finished=kwargs['finished'])
    #     new_task.save()
    #     return new_task
