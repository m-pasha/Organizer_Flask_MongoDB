from flask import jsonify
from flask import request
from flask.views import MethodView

from app.task.models import Task, CategoryTask


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


class CategoryTaskView(MethodView):

    def get(self, title=None):
        try:
            if title is None:
                category = CategoryTask.objects()
                return category.to_json()
            else:
                category = CategoryTask.objects(title=title)
                return category.to_json()
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def post(self):
        try:
            data = request.json
            category = CategoryTask(**data)
            category.save()
            return jsonify({"status": "Created", "detail": "Your category was created"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def delete(self, title):
        try:
            category = CategoryTask.objects(title=title)
            category.delete()
            return jsonify({"status": "Deleted", "detail": "Your category was deleted"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def put(self, title):
        pass
