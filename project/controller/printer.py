# -*- coding: utf-8 -*-
from project import app
from project.models import Printer
from flask import render_template, request
from flaskext.wtf import Form, TextField, validators

class CreateForm(Form):
  text = TextField(u'Text:', [validators.Length(min=1, max=20)])

@app.route('/')
def start():
  return render_template('printer/index.html')

@app.route('/print', methods=['GET','POST'])
def printer():
  form = CreateForm(request.form)
  if request.method=='POST' and form.validate():
    printer = Printer()
    printer.show_string(form.text.data)
    return render_template('printer/index.html')
  return render_template('printer/print.html', form=form)


