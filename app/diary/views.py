from flask import jsonify
from flask import request
from flask.views import MethodView

from app.diary.models import Diary


class DiaryView(MethodView):
    
    def get(self, title=None):
        try:
            if title is None:
                diary = Diary.objects()
                return diary.to_json()
            else:
                diary = Diary.objects(title=title)
                return diary.to_json()
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def post(self):
        try:
            data = request.json
            diary = Diary(**data)
            diary.save()
            return jsonify({"status": "Created", "detail": "Your diary was created"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def delete(self, title):
        try:
            diary = Diary.objects(title=title)
            diary.delete()
            return jsonify({"status": "Deleted", "detail": "Your diary was deleted"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})

    def patch(self, title):
        try:
            data = request.json
            Diary.objects(title=title).update(**data)
            return jsonify({"status": "Updated", "detail": "Your diary was updated"})
        except Exception as e:
            return jsonify({"status": "Error", "detail": e})
