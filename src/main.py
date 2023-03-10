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
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('AUTH_USER', 'admin')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('AUTH_PASSWORD', 'admin')
chart_title = os.environ.get('CHART_TITLE', 'Cigar cabinet')
socket_url = os.environ.get('SOCKET_URL', 'http://127.0.0.1:5000')
basic_auth = BasicAuth(app)


def get_data():
    t = [dict(y=record['t'], x=record['date']) for record in Records().records]
    h = [dict(y=record['h'], x=record['date']) for record in Records().records]
    return dict(t=t, h=h)


def background_thread():
    socketio.emit('status', {'data': get_data()})


@socketio.event
def connect():
    logger.warning("client connected")
    emit('is_alive')
    emit('status', {'data': get_data()})


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', title=chart_title, socket_url=socket_url)


@app.route('/add', methods=['GET'])
@basic_auth.required
def add():
    from datetime import datetime

    t, h = request.args.get('t'), request.args.get('h')
    if not (t and h):
        return {'error': "Missing one of the values", }, 400
    now = str(datetime.now().isoformat())
    Records().write(dict(t=t, h=h, date=now)).save()

    socketio.start_background_task(background_thread)
    return {"ok": True}


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True, host='0.0.0.0')
