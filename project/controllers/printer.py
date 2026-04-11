from flask import Blueprint, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from project.models.printer import Printer

printer_bp = Blueprint("printer", __name__)


class CreateForm(FlaskForm):
    text = StringField("name", validators=[DataRequired()])


@printer_bp.route("/")
def start():
    return render_template("printer/index.html")


@printer_bp.route("/print", methods=["GET", "POST"])
def printer():
    form = CreateForm(request.form)
    if request.method == "POST" and form.validate():
        Printer().show_string(form.text.data)
        return redirect(url_for("printer.start"))
    return render_template("printer/print.html", form=form)
