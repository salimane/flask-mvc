# Flask-MVC

[![Build Status](https://github.com/salimane/flask-mvc/actions/workflows/master.yml/badge.svg)](https://github.com/salimane/flask-mvc/actions)
[![codecov](https://codecov.io/gh/salimane/flask-mvc/branch/master/graph/badge.svg)](https://codecov.io/gh/salimane/flask-mvc)
[![Maintenance](https://img.shields.io/maintenance/yes/2026.svg)](https://github.com/salimane/flask-mvc/commits/master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A minimal Flask boilerplate following the **MVC pattern** — designed as a clean starting point
for new Python web applications.

---

## Features

- **Application Factory** (`create_app()`) — safe for testing and multiple configs
- **Blueprint-based controllers** — one file per resource, explicit registration
- **Environment-based configuration** — `Development`, `Testing`, `Production` config classes
- **POST/Redirect/GET** form handling — prevents double-submit on refresh
- **Jinja2 macro library** — shared `render_error` and helpers in `layout/macros.html`
- **Test suite** — 96% coverage out of the box with pytest + pytest-cov
- **Docker-ready** — optimised multi-layer `Dockerfile` and `docker-compose.yml`

---

## Project structure

```
flask-mvc/
├── project/
│   ├── __init__.py          # create_app() factory
│   ├── config.py            # Dev / Testing / Production config classes
│   ├── controllers/
│   │   └── printer.py       # printer Blueprint + form
│   ├── models/
│   │   └── printer.py       # Printer model
│   ├── static/css/
│   └── templates/
│       ├── layout/
│       │   ├── layout.html  # base template
│       │   └── macros.html  # reusable Jinja2 macros
│       └── printer/
├── tests/
│   ├── conftest.py          # app / client fixtures
│   └── test_printer.py
├── .env.example             # required env vars — copy to .env before running
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-test.txt
└── runserver.py
```

---

## Prerequisites

- Python 3.14+
- pip

Optional (for Python version management):

```bash
brew install asdf
asdf plugin add python
asdf install python 3.14.4
```

---

## Setup

```bash
# 1. Clone
git clone git@github.com:salimane/flask-mvc.git
cd flask-mvc

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements-test.txt

# 4. Configure environment
cp .env.example .env
# Open .env and set SECRET_KEY — generate one with:
#   python -c "import secrets; print(secrets.token_hex(32))"
```

---

## Running

```bash
# Development server (reads PORT from env, default 8080)
source .env && python runserver.py

# Or via Make
make run
```

### Docker

```bash
cp .env.example .env   # fill in SECRET_KEY
docker-compose up --build
```

The app is served by **gunicorn** on port `16000` inside the container.

---

## Testing

```bash
SECRET_KEY=test pytest tests/ -v --cov=project --cov-report=term-missing
```

Or via the helper script (creates an isolated virtualenv automatically):

```bash
script/test
```

### Coverage

```
Name                              Stmts   Miss  Cover
-----------------------------------------------------
project/__init__.py                  15      1    93%
project/config.py                    20      1    95%
project/controllers/printer.py       18      0   100%
project/models/printer.py             4      0   100%
-----------------------------------------------------
TOTAL                                57      2    96%
```

---

## Configuration

All configuration is driven by environment variables. See `.env.example` for the full list.

| Variable     | Required | Default       | Description                      |
|--------------|----------|---------------|----------------------------------|
| `SECRET_KEY` | **Yes**  | —             | Flask session / CSRF signing key |
| `FLASK_ENV`  | No       | `development` | Config profile (`development`, `testing`, `production`) |
| `PORT`       | No       | `8080`        | Dev server port                  |

Generate a secure key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## Extending the boilerplate

To add a new resource (e.g. `user`):

1. **Model** — `project/models/user.py`
2. **Controller** — `project/controllers/user.py` with `user_bp = Blueprint('user', __name__)`
3. **Register** — add `app.register_blueprint(user_bp)` in `create_app()` (`project/__init__.py`)
4. **Templates** — `project/templates/user/`
5. **Tests** — `tests/test_user.py`

See [`.github/copilot-instructions.md`](.github/copilot-instructions.md) for the full development
guide and coding conventions.

---

## Contributing

Issues and pull requests are welcome. Please keep PRs focused — one concern per PR.

## Maintainers

[Salimane Adjao Moustapha](https://github.com/salimane)

## License

Copyright © 2026 Salimane Adjao Moustapha. Licensed under the [MIT License](LICENSE).

