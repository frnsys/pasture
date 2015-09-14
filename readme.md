# Pasture

![Pasture](pasture.jpg)

([Image source](https://commons.wikimedia.org/wiki/File:PolledHereford_bull.jpg), modified and licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en).)

When teaching Python to students, I've found the hardest part is all the setup involved. Some students have different computers, depending on the class, many might have never programmed before and don't have any dev environment at all. Walking everyone through preparing their systems takes _forever_. This is often even the case with experienced devs!

__Pasture__ simplifies this - all you need to do is install it on one machine. It runs [`jupyterhub`](https://github.com/jupyter/jupyterhub) inside a Docker container which allows each student to have their own [`jupyter`](https://github.com/jupyter/notebook) notebook server to work with. The Docker container's `jupyterhub` port (8000) is mapped to the host's port 8000, which can then be exposed by configuring your firewall to open that port and then by adapting the example `nginx` config (`assets/example_nginx.conf`).

Pasture used to be a custom-built solution but with the excellent `jupyterhub` and Docker, it only needs to be a small set of scripts now :)

## Usage

Clone this repo to your host machine.

Then you can run the `pasture` script from within the repo.

If you don't have Docker installed, run `./pasture setup` first.

```
./pasture <command>

Available commands:
- setup      - setup your host system
- build      - build your image
- run        - start the container and run jupyterhub inside it
- clean      - stop and remove the container
- shell      - launch a shell in the container
- mkusers #  - create # users (usernames are randomly-generated;
               password is the username, used as logins for jupyterhub)
- lsusers    - list all users. also accepts additional flags:
    - -s     - list users with active jupyter servers
    - -u     - list unclalimed users (users not running jupyter servers)
    - -m     - realtime list of unclaimed users
```

### Example usage

```
# build your image
./pasture build

# run the container
./pasture run

# setup nginx conf
sudo cp assets/example_nginx.conf /etc/nginx/conf.d/my.server.com.conf

# edit nginx conf if needed
sudo vi /etc/nginx/conf.d/my.server.com.conf

# restart nginx
sudo service nginx restart

# make users for folks to login as
./pasture mkusers 10

# display a realtime list of unclaimed users
# make it big, throw up on a projector for others to see
./pasture lsusers -m
```

## Customization

The Docker image installs the Python packages specified in `assets/requirements.txt`, which is just a typical Python requirements file. By default, it sets up a Python data science stack - but you can edit/replace that file to match your needs.

Just note that if any of your Python packages has additional system dependencies, you need to include them in the Dockerfile.

If you have data or other assets you want available to students, place them in `assets/data`.

## Details

This is setup to run `jupyterhub` without `sudo` for greater security (though the Docker container helps with security). Additional users created are unprivileged.

The main user is `pasture` with the password you specify with the `build` command; this username/password combo is also used to log into `jupyterhub` as the admin.
