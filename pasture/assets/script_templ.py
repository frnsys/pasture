import sys

# So we can import tools from the app.
# I'd like to find a better way eventually.
sys.path.append('$toolkit_path')
import toolkit

# A print method that handles encoding.
def print_(x):
    if type(x) is unicode:
        print(x.encode('utf-8'))
    else:
        print(x)

HELP = """
- HELP ------------------------------
Use `print_` instead of `print` to print without worrying about encoding.
- END -------------------------------
"""

# THE USER SCRIPT
$script
# ===============
