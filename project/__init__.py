# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
app = Flask('project')
app.config['SECRET_KEY'] = 'random'
from project.controllers import *