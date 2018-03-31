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

    def put(self, title):
        pass


class Currency(MethodView):
    pass

class BudgetAccount(MethodView):
    pass

class Invoice(MethodView):
    pass