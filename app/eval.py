import sys
import os
import subprocess
from datetime import datetime
from string import Template

from sanitize import sanitize
import config

dir       = os.path.dirname(os.path.realpath(__file__))
templpath = os.path.join(dir, 'assets/script_templ.py')
datapath  = os.path.join(dir, 'assets/gamergate.json')
graphpath = os.path.join(dir, 'assets/gamergate_socialgraph.json')

# Use this python executable so we have access to the same venv.
# sys.executable doesn't work when using uswgi.
# pyexec    = sys.executable
# Instead, set it up manually in the config.
pyexec = os.path.join(config.VENV, 'bin/python')

def execute(script, id):
    filepath = os.path.join('/tmp/', id)
    outpath = '/tmp/{0}_out'.format(id)
    script = sanitize(script)

    with open(templpath, 'r') as f:
        templ = Template(f.read())
    script = templ.substitute(
            script=script,
            datapath=datapath,
            graphpath=graphpath,
            toolspath=dir,
            outpath=outpath)

    with open(filepath, 'w') as f:
        f.write(script)

    p = subprocess.Popen([pyexec, filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    return out, err, outpath
