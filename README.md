# What's this?

This is an example event sourcing project.

I blogged about this at https://yoongkang.com/blog/event-sourcing-in-django/


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