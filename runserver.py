#!/usr/bin/env python
import os

from project import create_app

app = create_app(os.environ.get("FLASK_ENV", "development"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run("0.0.0.0", port=port)
