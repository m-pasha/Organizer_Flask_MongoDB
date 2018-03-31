from datetime import datetime
from mongoengine import Document
from mongoengine.fields import StringField, BooleanField, DateTimeField, ReferenceField, IntField

from app.accounts.models import Account


class CategoryBudget(Document):
    owner = ReferenceField(Account, reverse_delete_rule=mongoengine.CASCADE)
    title = StringField(min_length=1, max_length=50, required=True)

    def __str__(self):
        return self.title


class Currency(Document):
    owner = ReferenceField(Account, reverse_delete_rule=mongoengine.CASCADE)
    short_name = StringField(min_length=1, max_length=5, required=True)
    name = StringField(min_length=1, max_length=50)

    def __str__(self):
        return self.short_name


class BudgetAccount(Document):
    owner = ReferenceField(Account, reverse_delete_rule=mongoengine.CASCADE)
    currency = ReferenceField(Currency, reverse_delete_rule=mongoengine.CASCADE)
    name = StringField(min_length=1, max_length=100)
    short_name = StringField(min_length=1, max_length=50)
    amount = IntField(default=0)
    description = StringField(max_length=200)

    def __str__(self):
        return "%s - %s" % (self.currency, self.short_name)


class Invoice(Document):
    owner = ReferenceField(Account, reverse_delete_rule=mongoengine.CASCADE)
    budget_account = ReferenceField(BudgetAccount, reverse_delete_rule=mongoengine.CASCADE)
    currency = ReferenceField(Currency, reverse_delete_rule=mongoengine.CASCADE)
    category = ReferenceField(CategoryBudget)       # TODO: on_delete
    transaction_type = StringField()        # TODO: make choice _income or _outcome
    description = StringField(max_length=200)
    amount = IntField(default=0)
    creation = DateTimeField(default=datetime.utcnow())

    def __str__(self):
        return "%s - %s - %s" % (self.currency, self.transaction_type, self.amount)
