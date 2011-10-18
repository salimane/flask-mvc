# -*- coding: utf-8 -*-

__version__ = '0.1'

from flask import Flask, Markup
app = Flask('project')
app.config['SECRET_KEY'] ='random'

import project.models
import project.views


