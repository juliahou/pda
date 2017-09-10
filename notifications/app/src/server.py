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

# class JsonEncodedDict(db.TypeDecorator):
#     """Enables JSON storage by encoding and decoding on the fly."""
#     impl = db.Text

#     def process_bind_param(self, value, dialect):
#         if value is None:
#             return '{}'
#         else:
#             return json.dumps(value)

#     def process_result_value(self, value, dialect):
#         if value is None:
#             return {}
#         else:
#             return json.loads(value)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=False)
    # token = db.Column(JsonEncodedDict)
    # location = db.Column(JsonEncodedDict)
    token = db.Column(db.Text, unique=True)
    location = db.Column(db.Text, unique=False)

    def __init__(self, username='', password='', token='', location=''):
        self.username = username
        self.password = password
        self.token = token
        self.location = location

def init_db():
    db.create_all()

    # Create a test user
    # new_user = User('jjhou', 'meow', 'dg', 'erg')
    # new_user.display_name = 'Julia'
    # db.session.add(new_user)
    # db.session.commit()

# Basic arguments. You should extend this function with the push features you
# want to use, or simply pass in a `PushMessage` object.
def send_push_message(token, message, extra=None):
    try:
        response = PushClient().publish(
            PushMessage(to=token,
                        body=message,
                        data=extra))
    except PushServerError as exc:
        # Encountered some likely formatting/validation error.
        rollbar.report_exc_info(
            extra_data={
                'token': token,
                'message': message,
                'extra': extra,
                'errors': exc.errors,
                'response_data': exc.response_data,
            })
        raise
    except (ConnectionError, HTTPError) as exc:
        # Encountered some Connection or HTTP error - retry a few times in
        # case it is transient.
        rollbar.report_exc_info(
            extra_data={'token': token, 'message': message, 'extra': extra})
        raise self.retry(exc=exc)

    try:
        # We got a response back, but we don't know whether it's an error yet.
        # This call raises errors so we can handle them with normal exception
        # flows.
        response.validate_response()
    except DeviceNotRegisteredError:
        # Mark the push token as inactive
        from notifications.models import PushToken
        PushToken.objects.filter(token=token).update(active=False)
    except PushResponseError as exc:
        # Encountered some other per-notification error.
        rollbar.report_exc_info(
            extra_data={
                'token': token,
                'message': message,
                'extra': extra,
                'push_response': exc.push_response._asdict(),
            })
        raise self.retry(exc=exc)

@app.route('/distress', methods=['POST'])
def distress():
    users = User.query.all()
    json = request.get_json()
    for user in users:
        if json['id'] != user.id:
            send_push_message(user.token, "WOOO PUSH NOTIFICATION")
    return ('', 204)

@app.route('/adduser', methods=['POST'])
def add_user():
    json = request.get_json()
    print(json)
    new_user = User(json['username'], json['password'], json['token'], json['location'])
    new_user.display_name = 'cat'
    db.session.add(new_user)
    db.session.commit()
    return ('', 204)