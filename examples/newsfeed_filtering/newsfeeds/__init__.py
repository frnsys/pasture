import os

from pasture import Pasture

from . import util
from .routes import bp

dir = os.path.dirname(os.path.realpath(__file__))
datapath  = os.path.join(dir, 'assets/gamergate.json')
graphpath = os.path.join(dir, 'assets/gamergate_socialgraph.json')

def pre_eval_func(pasture, script, id, substitutions):
    pasture.socketio.emit('updating', {}, room=id)

    outpath = util.build_outpath(id)
    substitutions['datapath']  = datapath
    substitutions['graphpath'] = graphpath
    substitutions['outpath']   = outpath

def post_eval_func(pasture, script, id, substitutions, out, err):
    outpath = substitutions['outpath']
    tweets = util.load_tweets(outpath) if not err else []

    # Refresh feed pages with the new tweets.
    pasture.socketio.emit('executed', {'tweets': tweets}, room=id)

options = {
    'config':               {'DEBUG': True},
    'blueprints':           [bp],
    'pre_eval_func':        pre_eval_func,
    'post_eval_func':       post_eval_func,
    'script_template_path': os.path.join(dir, 'assets/script_templ.py'),
    'toolkit_path':         os.path.join(dir, 'assets/toolkit.py'),
    'auth_user':            'student',
    'auth_pass':            'super-secret-password',
    'venv_path':            '~/env/pasture_newsfeeds'
}

pasture = Pasture(**options)
