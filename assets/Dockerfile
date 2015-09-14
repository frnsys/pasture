FROM ubuntu:14.04
MAINTAINER francis <f@frnsys.com>

# setup
RUN apt-get update
RUN apt-get upgrade -yq
RUN apt-get install -yq --no-install-recommends python gcc gfortran build-essential g++ make wget git openssh-server python-software-properties software-properties-common libxml2-dev libxslt1-dev libyaml-dev bzip2 openssh-server curl wget python-dev openssl
#RUN apt-get build-dep python-matplotlib -yq
#
# python
RUN apt-get install -yq python3 python3-setuptools python-pip python3-pip cython3
#RUN pip3 install cython

# install pre-compiled packages,
# may be a bit out of date, but the image builds _much_ quicker
RUN apt-get install -yq python3-numpy python3-scipy python3-matplotlib

# maths
RUN apt-get install -yq libatlas-base-dev liblapack-dev libopenblas-dev libopenblas-base libatlas3gf-base

# node/npm (jupyterhub deps)
RUN apt-get install -yq npm nodejs-legacy
RUN npm install -g configurable-http-proxy

# add primary user
RUN useradd -ms /bin/bash -p $(openssl passwd -1 pasturepw) pasture
RUN adduser pasture sudo
RUN usermod -a -G shadow pasture
RUN echo "pasture ALL=(ALL) NOPASSWD: /usr/local/bin/sudospawner" >> /etc/sudoers

# jupyter & jupyterhub
RUN pip3 install jupyter jupyterhub
RUN pip3 install git+https://github.com/jupyter/sudospawner
RUN mkdir /etc/jupyterhub
RUN chown -R pasture /etc/jupyterhub

# add files
ADD assets/data /home/pasture/data
ADD assets/users/mkuser /usr/local/bin/mkuser

# setup env
ADD assets/requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

USER pasture
ENV HOME /home/pasture

# - Change into the jupyterhub dir, which is owned by the pasture user,
# so we don't need to launch jupyterhub as sudo.
# - Use the sudospawner so unprivileged users can spawn their own notebooks
# - Set the pasture user to be an admin.
# - Create system users if new users are added and they don't exist as system users
CMD cd /etc/jupyterhub; jupyterhub --JupyterHub.spawner_class=sudospawner.SudoSpawner --Authenticator.admin_users="['pasture']" --PAMAuthenticator.create_system_users=True
#CMD /bin/bash

# Expose ports, 22->ssh, 8000->jupyterhub
EXPOSE 22 8000