import os
import json

from flask import render_template, request, redirect, jsonify, url_for
from flask.ext.socketio import emit, join_room

from app import app, socketio
from .auth import requires_auth
from .eval import execute
from .names import random_name

import logging
logger = logging.getLogger('newsautomata_filters')
fh = logging.FileHandler('/var/log/newsautomata_filters.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)

@app.route('/', methods=['GET'])
@requires_auth
def index():
    return redirect(url_for('session', id=random_name()))

@app.route('/code/<string:id>', methods=['GET'])
@requires_auth
def session(id):
    return render_template('index.html', id=id)

@app.route('/feed/<string:id>', methods=['GET'])
@requires_auth
def feed(id):
    out, err, outpath = execute('', id)
    tweets = load_tweets(outpath)
    return render_template('feed.html', tweets=tweets)

@app.route('/eval/<string:id>', methods=['POST'])
@requires_auth
def eval(id):
    socketio.emit('updating', {}, room=id)

    script = request.form['script']
    out, err, outpath = execute(script, id)
    tweets = load_tweets(outpath) if not err else []

    # Refresh feed pages with the new tweets.
    socketio.emit('executed', {'tweets': tweets}, room=id)

    return jsonify({
        'out': out,
        'err': err
    })

@app.route('/graph', methods=['GET'])
@requires_auth
def graph():
    return render_template('graph.html')

@socketio.on('join')
def join(msg):
    join_room(msg['room'])

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    logger.exception(error)
    return render_template('500.html'), 500


# Load up the script's filtered tweets.
# Using the file system like this is kind of slow...
def load_tweets(outpath):
    with open(outpath, 'r') as f:
        tweets = json.load(f)
    return tweets
