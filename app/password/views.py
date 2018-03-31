from flask import jsonify
from flask import request
from flask.views import MethodView

from app.password.models import Password


class PasswordView(MethodView):

    def get(self, resource_url=None):
        try:
            if resource_url is None:
                password = Password.objects()
                return password.to_json()
            else:
                password = Password.objects(resource_url=resource_url)
                return password.to_json()
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def post(self):
        try:
            data = request.json
            password = Password(**data)
            password.save()
            return jsonify({"status": "Created", "detail": "Your password was created"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def delete(self, resource_url):
        try:
            password = Password.objects(resource_url=resource_url)
            password.delete()
            return jsonify({"status": "Deleted", "detail": "Your password was deleted"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def put(self, resource_url):
        pass
