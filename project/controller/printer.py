from project import app
from project.models import Printer
from flask import render_template, request
@app.route('/')
def start():
    return render_template('index.html')

@app.route('/print',methods=['GET','POST'])
def printer():
    if request.method=='POST':
         printer = Printer()
         printer.show_string(request.form['text'])
         return render_template('index.html')
    return render_template('print.html')


