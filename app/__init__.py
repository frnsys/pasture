from flask import Flask
from flask.ext.socketio import SocketIO

app = Flask(__name__, static_folder='static', static_url_path='')

# Load config.
app.config.from_object('config')

socketio = SocketIO(app)

from app import routes
