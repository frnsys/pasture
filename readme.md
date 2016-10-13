# Pasture

![Pasture](pasture.jpg)

([Image source](https://commons.wikimedia.org/wiki/File:PolledHereford_bull.jpg), modified and licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en).)

When teaching Python to students, I've found the hardest part is all the setup involved. Some students have different computers, depending on the class, many might have never programmed before and don't have any dev environment at all. Walking everyone through preparing their systems takes _forever_. This is often even the case with experienced devs!

This project has mostly been superseded by newer versions of [`jupyterhub`](https://github.com/jupyter/jupyterhub). Now it just manages system users for use with `jupyterhub`.

## Usage

Clone this repo to your host machine.

Then you can run the `pasture` script from within the repo.

```
./pasture <command>

Available commands:
- mkusers #  - create # users (usernames are randomly-generated;
               password is the username, used as logins for jupyterhub)
- rmusers    - remove users created by pasture
- lsusers    - list all users. also accepts additional flags:
    - -s     - list users with active jupyter servers
    - -u     - list unclalimed users (users not running jupyter servers)
    - -m     - realtime list of unclaimed users
```

### Example usage

```
# make users for folks to login as
./pasture mkusers 10

# display a realtime list of unclaimed users
# make it big, throw up on a projector for others to see
./pasture lsusers -m

# have people go to some.site.com and login as one of the users

# clean up created users
./pasture rmusers
```
