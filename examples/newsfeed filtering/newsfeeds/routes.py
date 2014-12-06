import os
import json

from flask import Blueprint, render_template

from pasture.auth import requires_auth

bp = Blueprint('newsfilter',
        __name__,
        template_folder='templates',
        static_folder='static')

@bp.route('/feed/<string:id>', methods=['GET'])
@requires_auth
def feed(id):
    out, err, outpath = execute('', id)
    tweets = load_tweets(outpath)
    return render_template('feed.html', tweets=tweets)

@bp.route('/graph', methods=['GET'])
@requires_auth
def graph():
    return render_template('graph.html')

# Load up the script's filtered tweets.
# Using the file system like this is kind of slow...
def load_tweets(outpath):
    with open(outpath, 'r') as f:
        tweets = json.load(f)
    return tweets
