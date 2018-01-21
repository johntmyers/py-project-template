# py-project-template

Template I use for generic Python projects

- Rename `proj` directory to your preferred project package name
- Rename `main.py` if desired to your first module
- Update project name in `get_cli_parser` function in `main.py`
- Modify `setup.py` as necessary
- Modify `Dockerfile`, can change `proj` usage to whatever you call your package

# setup

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -I .
```

# running

```
$ python -m proj.main --string foo
```

# docker

```
$ docker build -t myorg/myproject .
$ sudo docker run -it myorg/myproject python -m proj.main --string foo
```

# docker stack

Run your app with other services, controlling ceratin settings through
Environment variables. These variables can be defined in a `.env` file
within the root directory of your project. Docker Compose will grab
these environment variables and utlize them in the containers that get launched.

This template has a simple stack that uses Redis to listen for events off of
a pub/sub bus and just echoes them out via a logger.