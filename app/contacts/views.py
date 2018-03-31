from flask import jsonify
from flask import request
from flask.views import MethodView

from app.contacts.models import Contact


class ContactView(MethodView):

    def get(self, name=None):
        try:
            if name is None:
                contact = Contact.objects()
                return contact.to_json()
            else:
                contact = Contact.objects(name=name)
                return contact.to_json()
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def post(self):
        try:
            data = request.json
            contact = Contact(**data)
            contact.save()
            return jsonify({"status": "Created", "detail": "Your contact was created"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def delete(self, name):
        try:
            contact = Contact.objects(name=name)
            contact.delete()
            return jsonify({"status": "Deleted", "detail": "Your contact was deleted"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def put(self, name):
        pass
