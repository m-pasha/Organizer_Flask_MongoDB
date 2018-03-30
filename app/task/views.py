from flask import jsonify
from flask import request
from flask.views import MethodView

from app.task.models import Task


class TaskView(MethodView):

    def get(self, title=None):
        try:
            if title is None:
                task = Task.objects()
                return task.to_json()
            else:
                task = Task.objects(title=title)
                return task.to_json()
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def post(self):
        try:
            data = request.json
            task = Task(**data)
            task.save()
            print(data)
            return jsonify({"status": "Created", "detail": "Your task was created"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def delete(self, title):
        try:
            task = Task.objects(title=title)
            task.delete()
            return jsonify({"status": "Deleted", "detail": "Your task was deleted"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def put(self, title):
        pass
