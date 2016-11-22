# Configuration file for jupyterhub.
# /etc/jupyterhub_config.py

c.JupyterHub.ssl_key = '/etc/letsencrypt/live/pasture.publicscience.co/privkey.pem'
c.JupyterHub.ssl_cert = '/etc/letsencrypt/live/pasture.publicscience.co/fullchain.pem'
c.Authenticator.admin_users = {'ftseng'}
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 443
c.Spawner.notebook_dir = '~/workshop'
