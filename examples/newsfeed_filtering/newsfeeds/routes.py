from flask import Blueprint, render_template

from . import util

bp = Blueprint('newsfeeds',
        __name__,
        template_folder='templates',
        static_folder='static',
        static_url_path='/newsfeeds')

@bp.route('/feed/<string:id>', methods=['GET'])
def feed(id):
    outpath = util.build_outpath(id)
    tweets = util.load_tweets(outpath)
    return render_template('feed.html', tweets=tweets)

@bp.route('/graph', methods=['GET'])
def graph():
    return render_template('graph.html')
