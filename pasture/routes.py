from flask import Blueprint, render_template, request, redirect, jsonify, url_for
from flask.ext.socketio import emit, join_room

from . import socketio
from .eval import execute
from .names import random_name

def create_blueprint(pasture):
    """
    Create the main blueprint for a Pasture.
    """
    bp = Blueprint('pasture', __name__)

    @bp.route('/', methods=['GET'])
    def index():
        return redirect(url_for('pasture.session', id=random_name()))

    @bp.route('/code/<string:id>', methods=['GET'])
    def session(id):
        return render_template('index.html', id=id)

    @bp.route('/eval/<string:id>', methods=['POST'])
    def eval(id):
        script = request.form['script']
        out, err = pasture.eval_func(pasture, script, id, substitutions={})

        return jsonify({
            'out': out,
            'err': err
        })

    @socketio.on('join')
    def join(msg):
        join_room(msg['room'])

    return bp

def create_errorhandlers(pasture):
    @pasture.app.errorhandler(404)
    def internal_error(error):
        return render_template('404.html'), 404

    @pasture.app.errorhandler(500)
    def internal_error(error):
        logger.exception(error)
        return render_template('500.html'), 500
