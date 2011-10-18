#!/usr/bin/env python
# -*- coding: utf-8 -*-

from project import app
from project.models import printer

if __name__=='__main__':
    app.run('0.0.0.0',debug=True)
