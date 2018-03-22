from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from mongoengine import connect

from accounts.views import get_accounts_list
# from app.config import MONGO_SERVER, MONGO_SERVER_PORT, MONGO_DB_NAME, MONGO_USER_NAME, MONGO_PASSWORD

app = Flask(__name__)
# app.config.from_pyfile('the-config.cfg')
app.config['MONGODB_SETTINGS'] = {
    'db': 'organizer',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine(app)


@app.route("/")
def hello():
    return render_template('test.html')


@app.route("/accounts")
def accounts_list():
    pass


if __name__ == '__main__':

    app.run(host='127.0.0.1', debug=True, port=88)
