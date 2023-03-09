from threading import Lock
import os
from flask import Flask, render_template, request
from flask_basicauth import BasicAuth
from flask_socketio import SocketIO, emit
import logging

from utils import Records

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'most_secret_key'
socketio = SocketIO(app)
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('auth_user', 'admin')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('auth_user', 'admin')
basic_auth = BasicAuth(app)

thread = None
lock = Lock()


def get_data():
    t = [dict(y=record['t'], x=record['date']) for record in Records().records]
    h = [dict(y=record['h'], x=record['date']) for record in Records().records]
    return dict(t=t, h=h)


def background_thread():
    global thread

    socketio.emit('status', {'data': get_data()})
    thread = None


@socketio.event
def connect():
    logger.warning("client connected")
    emit('is_alive')
    emit('status', {'data': get_data()})


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/add', methods=['GET'])
@basic_auth.required
def add():
    from datetime import datetime
    global thread

    t, h = request.args.get('t'), request.args.get('h')
    if not (t and h):
        return {'error': "Missing one of the values", }, 400
    now = str(datetime.now().isoformat())
    Records().write(dict(t=t, h=h, date=now)).save()

    with lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    return {"ok": True}


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True, host='0.0.0.0')
