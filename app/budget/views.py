from flask import jsonify
from flask import request
from flask.views import MethodView

from app.budget.models import CategoryBudget, Currency, BudgetAccount, Invoice


class CategoryBudgetView(MethodView):

    def get(self, title=None):
        try:
            if title is None:
                category = CategoryBudget.objects()
                return category.to_json()
            else:
                category = CategoryBudget.objects(title=title)
                return category.to_json()
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def post(self):
        try:
            data = request.json
            category = CategoryBudget(**data)
            category.save()
            return jsonify({"status": "Created", "detail": "Your category was created"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def delete(self, title):
        try:
            category = CategoryBudget.objects(title=title)
            category.delete()
            return jsonify({"status": "Deleted", "detail": "Your category was deleted"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def patch(self, title):
        try:
            data = request.json
            CategoryBudget.objects(title=title).update(**data)
            return jsonify({"status": "Updated", "detail": "Your category was updated"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})


class CurrencyView(MethodView):

    def get(self, short_name=None):
        try:
            if short_name is None:
                currency = Currency.objects()
                return currency.to_json()
            else:
                currency = Currency.objects(short_name=short_name)
                return currency.to_json()
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def post(self):
        try:
            data = request.json
            currency = Currency(**data)
            currency.save()
            return jsonify({"status": "Created", "detail": "Your currency was created"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def delete(self, short_name):
        try:
            currency = CategoryBudget.objects(short_name=short_name)
            currency.delete()
            return jsonify({"status": "Deleted", "detail": "Your currency was deleted"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def patch(self, short_name):
        try:
            data = request.json
            Currency.objects(short_name=short_name).update(**data)
            return jsonify({"status": "Updated", "detail": "Your currency was updated"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})


class BudgetAccountView(MethodView):

    def get(self, short_name=None):
        try:
            if short_name is None:
                budget_acc = BudgetAccount.objects()
                return budget_acc.to_json()
            else:
                budget_acc = BudgetAccount.objects(short_name=short_name)
                return budget_acc.to_json()
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def post(self):
        try:
            data = request.json
            budget_acc = BudgetAccount(**data)
            budget_acc.save()
            return jsonify({"status": "Created", "detail": "Your budget account was created"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def delete(self, short_name):
        try:
            budget_acc = BudgetAccount.objects(short_name=short_name)
            budget_acc.delete()
            return jsonify({"status": "Deleted", "detail": "Your budget account was deleted"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def patch(self, short_name):
        try:
            data = request.json
            BudgetAccount.objects(short_name=short_name).update(**data)
            return jsonify({"status": "Updated", "detail": "Your budget account was updated"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})


class InvoiceView(MethodView):

    def get(self, id=None):
        try:
            if id is None:
                invoice = Invoice.objects()
                return invoice.to_json()
            else:
                invoice = Invoice.objects(id=id)
                return invoice.to_json()
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def post(self):
        try:
            data = request.json
            invoice = Invoice(**data)
            invoice.save()
            return jsonify({"status": "Created", "detail": "Your invoice was created"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def delete(self, id):
        try:
            invoice = Invoice.objects(id=id)
            invoice.delete()
            return jsonify({"status": "Deleted", "detail": "Your invoice was deleted"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def patch(self, id):
        try:
            data = request.json
            Invoice.objects(id=id).update(**data)
            return jsonify({"status": "Updated", "detail": "Your invoice was updated"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})
