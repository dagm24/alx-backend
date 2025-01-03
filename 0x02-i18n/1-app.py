#!/usr/bin/env python3
""" Babel setup """
import babel
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Configuration Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello_world():
    """ return html """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
