#!/usr/bin/python
# -*- coding: utf-8 -*-

from project import app
from flask import render_template, request
from flaskext.wtf import Form, TextField, validators


class CreateForm(Form):

    text = TextField(u'Text:', [validators.Length(min=1, max=20)])


@app.route('/')
def start():
    return render_template('printer/index.html')


@app.errorhandler(404)
def page_not_found(e):
    return (render_template('errors/404.html'), 404)


@app.errorhandler(403)
def forbidden(e):
    return (render_template('errors/403.html'), 404)


@app.errorhandler(500)
def internal_server_error(e):
    return (render_template('errors/500.html'), 404)


@app.route('/print', methods=['GET', 'POST'])
def printer():
    form = CreateForm(request.form)
    if request.method == 'POST' and form.validate():
        from project.models.Printer import Printer
        printer = Printer()
        printer.show_string(form.text.data)
        return render_template('printer/index.html')
    return render_template('printer/print.html', form=form)
