# from src import app
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from exponent_server_sdk import DeviceNotRegisteredError
from exponent_server_sdk import PushClient
from exponent_server_sdk import PushMessage
from exponent_server_sdk import PushResponseError
from exponent_server_sdk import PushServerError
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'meow'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=False)
    token = db.Column(db.String(100), unique=True)
    location = db.Column(db.String(100), unique=False)

def init_db():
    db.create_all()

    # Create a test user
    # new_user = User('jjhou', 'meow', 'dg', 'erg')
    # new_user.display_name = 'Julia'
    # db.session.add(new_user)
    # db.session.commit()

# Basic arguments. You should extend this function with the push features you
# want to use, or simply pass in a `PushMessage` object.
def send_push_message(token, message):
#     # try:
    response = PushClient().publish(PushMessage(to=token,body=message))

@app.route('/distress', methods=['POST'])
def distress():
    users = User.query
    json = request.get_json()
    for user in users:
        if json['id'] != user.id:
            send_push_message(user.token, "WOOO PUSH NOTIFICATION")

@app.route('/add_user', methods=['POST'])
def add_user():
    json = request.get_json()
    new_user = User(json['username'], json['password'], json['token'], json['location'])
    new_user.display_name = 'cat'
    db.session.add(new_user)
    db.session.commit()

    # except PushServerError as exc:
    #     # Encountered some likely formatting/validation error.
    #     rollbar.report_exc_info(
    #         extra_data={
    #             'token': token,
    #             'message': message,
    #             'extra': extra,
    #             'errors': exc.errors,
    #             'response_data': exc.response_data,
    #         })
    #     raise
    # except (ConnectionError, HTTPError) as exc:
    #     # Encountered some Connection or HTTP error - retry a few times in
    #     # case it is transient.
    #     rollbar.report_exc_info(
    #         extra_data={'token': token, 'message': message, 'extra': extra})
    #     raise self.retry(exc=exc)

    # try:
    #     # We got a response back, but we don't know whether it's an error yet.
    #     # This call raises errors so we can handle them with normal exception
    #     # flows.
    #     response.validate_response()
    # except DeviceNotRegisteredError:
    #     # Mark the push token as inactive
    #     from notifications.models import PushToken
    #     PushToken.objects.filter(token=token).update(active=False)
    # except PushResponseError as exc:
    #     # Encountered some other per-notification error.
    #     rollbar.report_exc_info(
    #         extra_data={
    #             'token': token,
    #             'message': message,
    #             'extra': extra,
    #             'push_response': exc.push_response._asdict(),
    #         })
    #     raise self.retry(exc=exc)
