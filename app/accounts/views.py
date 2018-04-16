from flask.views import MethodView
from flask import jsonify

from app.accounts.models import Account


class UserListView(MethodView):

    def get(self):
        users = Account.objects()
        result = {'email': 'admin1@mail.com', 'name': 'Admin'}  # "Accounts list"
        if result:
            output = result
        else:
            output = "ObjectDoesNotExist"
        return jsonify({'result': output})
