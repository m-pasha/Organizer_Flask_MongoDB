from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from mongoengine import connect

from app.config import MONGO_SERVER, MONGO_SERVER_PORT, MONGO_DB_NAME
from app.accounts.views import UserListView
from app.contacts.views import ContactView
from app.diary.views import DiaryView
from app.password.views import PasswordView
from app.task.views import TaskView, CategoryTaskView


db = MongoEngine()
app = Flask(__name__)
connect(MONGO_DB_NAME, host=MONGO_SERVER, port=MONGO_SERVER_PORT)
db.init_app(app)


@app.route("/")
def hello():
    return "<HTML><h1 align=center>Welcome to Flask</h1></HTML>"


app.add_url_rule('/account/list/', view_func=UserListView.as_view(name='account-list-view'))
app.add_url_rule('/contact/', defaults={'name': None}, view_func=ContactView.as_view('contact-list'), methods=['GET',])
app.add_url_rule('/contact/', view_func=ContactView.as_view('contact-create'), methods=['POST',])
app.add_url_rule('/contact/<name>', view_func=ContactView.as_view('contact-by-id'), methods=['GET', 'PUT', 'DELETE'])
app.add_url_rule('/diary/', defaults={'title': None}, view_func=DiaryView.as_view('diary-list'), methods=['GET',])
app.add_url_rule('/diary/', view_func=DiaryView.as_view('diary-create'), methods=['POST',])
app.add_url_rule('/diary/<title>', view_func=DiaryView.as_view('diary-by-id'), methods=['GET', 'PUT', 'DELETE'])
app.add_url_rule('/password/', defaults={'resource_url': None}, view_func=PasswordView.as_view('password-list'),
                 methods=['GET',])
app.add_url_rule('/password/', view_func=PasswordView.as_view('password-create'), methods=['POST',])
app.add_url_rule('/password/<resource_url>', view_func=PasswordView.as_view('password-by-id'),
                 methods=['GET', 'PUT', 'DELETE'])
app.add_url_rule('/task/', defaults={'title': None}, view_func=TaskView.as_view('task-list'), methods=['GET',])
app.add_url_rule('/task/', view_func=TaskView.as_view('task-create'), methods=['POST',])
app.add_url_rule('/task/<title>', view_func=TaskView.as_view('task-by-id'), methods=['GET', 'PUT', 'DELETE'])
app.add_url_rule('/category-task/', defaults={'title': None}, view_func=CategoryTaskView.as_view('category-task-list'),
                 methods=['GET',])
app.add_url_rule('/category-task/', view_func=CategoryTaskView.as_view('category-task-create'),
                 methods=['POST',])
app.add_url_rule('/category-task/<title>', view_func=CategoryTaskView.as_view('category-task-by-id'),
                 methods=['GET', 'PUT', 'DELETE'])


if __name__ == '__main__':

    app.run(host='127.0.0.1', debug=True, port=88)
