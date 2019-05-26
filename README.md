# What's this?

This is an example event sourcing project.

~~I blogged about this at https://yoongkang.com/blog/event-sourcing-in-django/~~

I took down my blog post as I wasn't happy with it. The link above will 404. Email me if you have any questions, at yoongkang [dot] lim [at] gmail.com


# Requirements

Requires Python 3.6 and Postgres 9.4+.

Create a database called `eventsourcing`, and change `settings.py` accordingly.


# Installation

Make sure you are in a virtualenv. If not, create a `venvs` directory in a place NOT in this project, and type:

```
python3.6 -m venv eventsourcing
source eventsourcing/bin/activate
```

And then

```
cd /path/to/repo
pip install requirements.txt
python manage.py migrate
```

# Using

Use the Django shell. This is explained in my blog post.
