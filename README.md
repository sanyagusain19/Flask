# simple Flask landing site

This is a small Flask app (learning project) that serves a static landing page and a couple of starter routes.

What's included:
- app.py — Flask entrypoint and routes (/ , /projects, /contact)
- templates/ — Jinja2 templates for pages
- static/ — CSS used by the templates
- requirements.txt — flask and gunicorn
- Procfile, Dockerfile, .env.example — basic deployment and dev helpers

Quick start

```bash
# install dependencies
pip install -r requirements.txt

# enable debug auto-reload locally (optional)
# either set env var FLASK_DEBUG=1 or run python app.py
python app.py

# production-like server with gunicorn
gunicorn "app:app" -b 0.0.0.0:5000
```

Environment

Use .env.example as a starting point. The app reads FLASK_DEBUG, FLASK_RUN_HOST and FLASK_RUN_PORT.

Deploy

- Docker: build and run the provided Dockerfile.
- Heroku-like platforms: Procfile included to run with Gunicorn.
