import re

def sanitize(script):
    """
    This isn't comprehensive enough but fine for now ~
    """
    for mod in ['subprocess', 'os', 'pickle', 'shutil']:
        script = re.sub(r'\n?.*(import|from) {0}.*'.format(mod), '', script)

    return script

def test_sanitize():
    malicious = """
    import subprocess
    import subprocess.foo
    from subprocess import foo
    import subprocess as foo
    import subprocess.foo as foo
    from subprocess.path import foo

    if True:
        import subprocess
        import subprocess.foo
        from subprocess import foo
        import subprocess as foo
        import subprocess.foo as foo
        from subprocess.path import foo
    """
    assert(sanitize(malicious).strip() == 'if True:')

test_sanitize()
