## Pasture

![Pasture](pasture.jpg)
[Source](https://commons.wikimedia.org/wiki/File:PolledHereford_bull.jpg), modified and licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en).

When teaching Python to students, I've found the hardest part is all the setup involved. Some students have different computers, depending on the class, many might have never programmed before and don't have any dev environment at all. Walking everyone through preparing their systems takes _forever_.

__Pasture__ simplifies this - all you need to do is install it on one machine and then setup that machine's dev environment. It runs a web server which allows students to write Python scripts _in-browser_ (:moneybag: no messy terminal!! :moneybag:) and have them evaluated by the remote environment - stdout and errors are communicated back to them.

Pasture does not support Python 3 at the moment since `gevent` does not yet support it.

### Installation

    pip install pasture

### Example usage

```python
from pasture import Pasture

# Configuration options
options = {
    # A config dict which is passed to the underlying Flask application.
    'config':               {'DEBUG': True},

    # Other Flask blueprints to include additional routes
    'blueprints':           [some_blueprint],

    # A function called before a submitted script is evaluated.
    'pre_eval_func':        pre_eval_func,

    # A function called after a submitted script is evaluated.
    'post_eval_func':       post_eval_func,

    # The path to your script template, where the user code is embedded.
    'script_template_path': os.path.join(dir, 'assets/script_templ.py'),

    # The path to a module which includes additional convenience functions
    # which may be dependent on other packages.
    'toolkit_path':         os.path.join(dir, 'assets/toolkit.py'),

    # Authentication information.
    'auth_user':            'student',
    'auth_pass':            'super-secret-password',

    # Path to the virtualenv you are using.
    # This is so that the scripts are executed with the proper Python binary.
    'venv_path':            '~/env/pasture_newsfeeds'
}

pasture = Pasture(**options)
pasture.run(port=5001)
```

For a more complete example, check out [`examples/newsfeed filtering/`](examples/newsfeed_filtering/).

### Security

Obviously having users run code on your server is not the safest thing. You should probably run Pasture as a user without many important permissions, to minimize potential damage. The assumption is that you're hosting Pasture only for whatever session you're using it for, amongst people you trust.
