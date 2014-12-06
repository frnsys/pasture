import os
import subprocess
from string import Template
from sanitize import sanitize

from flask import Flask
from flask.ext.socketio import SocketIO

socketio = SocketIO()

from routes import create_blueprint

class Pasture():
    def __init__(self,
            flask_config={},
            blueprints=[],
            pre_eval_func=None,
            post_eval_func=None,
            script_template_path='assets/script_templ.py',
            toolkit_path='assets/toolkit.py',
            venv_path='/'):

        self.app = Flask(__name__, static_folder='static', static_url_path='')
        self.script_template_path = script_template_path

        # Load default config and apply user config.
        self.app.config.from_object('config')
        app.config.update(**config)

        # Apply user customizations to the evaluation route.
        self.eval_func = build_eval_func(self,
                pre_eval_func=pre_eval_func,
                post_eval_func=post_eval_func)

        # Initialize and register the main blueprint.
        pasture_bp = create_blueprint(self)
        self.app.register_blueprint(pasture_bp)

        # Register user-specified blueprints.
        for bp in blueprints:
            self.app.register_blueprint(bp)

        # Use this python executable so we have access to the same venv.
        # sys.executable doesn't work when using uswgi.
        # pyexec    = sys.executable
        self.pyexec = os.path.join(venv_path, 'bin/python')

        socketio.init_app(self.app)

    def run(self, port=5001):
        # For debugging.
        #from gevent import monkey
        #monkey.patch_all()
        #app.debug = True

        self.socketio.run(self.app, port=port)

    def execute_script(self, script, user_id, substitutions={}):
        """
        Takes a script (string) for a user and executes it,
        returning any output and errors.
        """
        filepath = os.path.join('/tmp/', id)
        script = sanitize(script)

        substitutions['script']       = script
        substitutions['toolkit_path'] = self.toolkit_path

        with open(self.script_template_path, 'r') as f:
            templ = Template(f.read())

        script = templ.substitute(**substitutions)

        with open(filepath, 'w') as f:
            f.write(script)

        p = subprocess.Popen([self.pyexec, filepath],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        out, err = p.communicate()

        return out, err

    def build_eval_func(self, pre_eval_func=None, post_eval_func=None):
        """
        Build the evaluation function for handling submitted scripts.

        The [pre|post]_eval_funcs can be used to modify the script or
        construct other substitutions to go into the template.
        """
        def non_func(self, script, user_id, substitutions):
            pass

        if pre_eval_func is None:
            pre_eval_func = non_func
        if post_eval_func is None:
            post_eval_func = non_func

        def eval(self, script, user_id):
            pre_eval_func(self, script, user_id, substitutions)
            out, err = self.execute_script(script, user_id, substitutions=substitutions)
            post_eval_func(self, script, user_id, substitutions)
            return out, err

        return eval
