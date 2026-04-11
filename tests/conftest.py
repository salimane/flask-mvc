# -*- coding: utf-8 -*-
import os
import pytest

os.environ.setdefault('SECRET_KEY', 'test-secret-key-not-for-production')

from project import create_app  # noqa: E402


@pytest.fixture
def app():
    app = create_app('testing')
    yield app


@pytest.fixture
def client(app):
    return app.test_client()
