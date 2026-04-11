# GitHub Copilot Instructions — flask-mvc

## Project overview

A Flask boilerplate following the **MVC pattern** designed as a base skeleton for new Python web
applications. The primary goal is clarity and correctness over complexity.

---

## Architecture

### Application Factory

The app is created via `create_app(config_name)` in `project/__init__.py`. Never import a global
`app` object — always go through the factory. The factory:
1. Loads the correct `Config` class from `project/config.py`
2. Initialises Flask extensions (e.g. `DebugToolbarExtension`)
3. Registers all Blueprints

### MVC layout

```
project/
├── __init__.py          # create_app() factory
├── config.py            # Config classes (Development / Testing / Production)
├── controllers/         # Flask Blueprints — one file per resource
│   └── printer.py       # printer_bp Blueprint
├── models/              # Plain Python classes, no ORM currently
│   └── printer.py
├── static/
│   └── css/style.css
└── templates/
    ├── layout/
    │   ├── layout.html  # base template
    │   └── macros.html  # reusable Jinja2 macros (render_error, etc.)
    └── printer/
        ├── index.html
        └── print.html
```

### Blueprints

Every controller is a Blueprint registered in `create_app()`. Do **not** use the old glob
auto-import pattern. To add a new resource:

1. Create `project/controllers/<resource>.py` with a `<resource>_bp = Blueprint(...)`.
2. Register it in `create_app()`:
   ```python
   from project.controllers.<resource> import <resource>_bp
   app.register_blueprint(<resource>_bp)
   ```

---

## Conventions

### Python style

- **PEP 8** throughout. `flake8` enforces it with `max-line-length = 100`.
- Module filenames are always **`snake_case.py`** — never PascalCase.
- Imports at the **top** of every file — never inside functions or routes.
- Classes use **PascalCase**; functions and variables use **snake_case**.

### Configuration

- All runtime config comes from **environment variables**. No secrets in source code.
- `SECRET_KEY` is **required** at startup; the app raises `ValueError` immediately if missing.
- Use `FLASK_ENV` to select the config profile: `development` (default), `testing`, `production`.
- Reference `project/config.py` before adding any new config key.

### Controllers

- One Blueprint per resource in `project/controllers/`.
- Always use **POST/Redirect/GET** after a successful form submission to prevent double-posts:
  ```python
  return redirect(url_for('<blueprint>.<view>'))
  ```
- Form classes live in the same file as the Blueprint that owns them.
- Keep controllers thin — delegate logic to model classes.

### Models

- Plain Python classes. No Flask imports except `flash` / `current_app` where unavoidable.
- Models do **not** duplicate validation that the form layer already enforces.

### Templates

- All templates extend `layout/layout.html`.
- Reusable Jinja2 macros belong in `layout/macros.html` and are imported with
  `{% from "layout/macros.html" import <macro> %}`.
- Use `url_for('blueprint_name.view_name')` — never hardcode URLs.
- Write valid HTML5 (`<!doctype html>`, `<html lang="en">`, `<meta charset="utf-8">`).

---

## Environment variables

| Variable   | Required | Default       | Description                          |
|------------|----------|---------------|--------------------------------------|
| `SECRET_KEY` | Yes    | —             | Flask session / CSRF signing key     |
| `FLASK_ENV`  | No     | `development` | Config profile to load               |
| `PORT`       | No     | `8080`        | Port for the development server      |

Generate a secure key with:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## Development setup

```bash
cp .env.example .env          # fill in SECRET_KEY at minimum
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-test.txt
```

Run the dev server:
```bash
SECRET_KEY=<key> python runserver.py
# or: make run  (reads from .env if you source it first)
```

---

## Testing

```bash
SECRET_KEY=test-secret pytest tests/ -v --cov=project
```

- Tests live in `tests/`. Fixtures (`app`, `client`) are in `tests/conftest.py`.
- Use `TestingConfig` which sets `WTF_CSRF_ENABLED = False` and a fallback `SECRET_KEY`.
- Every new controller must have a corresponding test file `tests/test_<resource>.py`.
- Cover: GET renders correct template, POST with valid data redirects, POST with invalid data
  returns the form with errors.
- The `conftest.py` `app` fixture calls `create_app('testing')` — do not create a new app
  instance inside individual test files.

---

## Adding a new resource (checklist)

- [ ] `project/models/<resource>.py` — model class
- [ ] `project/controllers/<resource>.py` — Blueprint + form + routes
- [ ] Register Blueprint in `project/__init__.py → create_app()`
- [ ] `project/templates/<resource>/` — HTML templates
- [ ] `tests/test_<resource>.py` — test suite
- [ ] Export any new env vars in `.env.example`

---

## What is intentionally excluded

This boilerplate is minimal by design. The following are **not wired up yet** but can be added
when needed:

- Database / SQLAlchemy — postgres is already running in `docker-compose.yml` on port 5432
  (`flask_dev` db, user `flask`, password `flask`). Add Flask-SQLAlchemy + Flask-Migrate and
  set `DATABASE_URL` in `.env` to connect.
- Authentication (Flask-Login, Flask-Security)
- REST API layer (Flask-RESTful)
- Task queue (Celery / Flower)
- Frontend asset pipeline (Flask-Assets, cssmin, jsmin)

If you need one of these, add it in isolation with its own Blueprint and tests.
