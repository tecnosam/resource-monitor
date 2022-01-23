from flask import Flask

from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask('Resource Monitor')
app.config['SECRET_KEY'] = b'secret!'
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})

socketio = SocketIO(app, cors_allowed_origins="*")

x = socketio.test_client(app)

from .routes import *

from .socket_channels import *


