from . import app

from flask import jsonify

from .utils import *

@app.route('/')
def all():
    return jsonify(main_channel())

@app.route('/battery')
def battery_perc():
    return jsonify({'battery': battery_percent()})

@app.route('/network')
def network():
    return jsonify(network_info())

@app.route('/memory')
def memory():
    return jsonify(memory_info())

@app.route('/processor')
def processor():
    return jsonify(process_info())
