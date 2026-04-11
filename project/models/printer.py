from flask import flash


class Printer:

    def show_string(self, text):
        flash(text + "!!!")
