from . import app, socketio, x
from .socket_channels import sock_thread
from threading import Thread

Thread(target = socketio.run, args=(app, '0.0.0.0'), daemon=True).start()

Thread(target = sock_thread, args=(), daemon=True).start()

while True:

    continue