from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from mongoengine import connect

from app.accounts.views import UserListView
from app.task.views import TaskView
from app.config import MONGO_SERVER, MONGO_SERVER_PORT, MONGO_DB_NAME


db = MongoEngine()
app = Flask(__name__)
connect(MONGO_DB_NAME, host=MONGO_SERVER, port=MONGO_SERVER_PORT)
db.init_app(app)


@app.route("/")
def hello():
    return "<HTML><h1 align=center>Welcome to Flask</h1></HTML>"


app.add_url_rule('/account/list/', view_func=UserListView.as_view(name='account-list-view'))
app.add_url_rule('/task/', defaults={'title': None}, view_func=TaskView.as_view('task-list'), methods=['GET',])
app.add_url_rule('/task/', view_func=TaskView.as_view('task-create'), methods=['POST',])
app.add_url_rule('/task/<title>', view_func=TaskView.as_view('task-by-id'), methods=['GET', 'PUT', 'DELETE'])


if __name__ == '__main__':

    app.run(host='127.0.0.1', debug=True, port=88)
