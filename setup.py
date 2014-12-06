from sys import platform
from setuptools import setup

setup(
    name='pasture',
    version='0.1.0',
    description='a centralized python scripting environment',
    url='https://github.com/ftzeng/pasture',
    author='Francis Tseng',
    author_email='f@frnsys.com',
    license='GPLv3',

    packages=['pasture'],
    install_requires=[
        'flask',
        'flask-socketio',
        'flask-wtf',
        'jinja2',
        'gunicorn'
    ],
)
