from . import socketio

from flask_socketio import join_room, leave_room

from .utils import *

import time

def sock_thread():
    print("Running listener")
    prev_all = dict()
    while True:

        all = main_channel()

        for key in all:
            if all.get(key) != prev_all.get(key):
                socketio.emit(key, all.get(key), room = key)

        socketio.emit('all', main_channel(), room = 'all')

        prev_all = {key: all.get(key) for key in all}

        time.sleep(1)

rooms = ['battery', 'network', 'memory', 'processor', 'all']
@socketio.on('connect')
def conn():
    print("Tried to connect")

@socketio.on('join')
def on_join(data):
    room = data['room']
    print("yo")
    if room in rooms:
        join_room(room)

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)