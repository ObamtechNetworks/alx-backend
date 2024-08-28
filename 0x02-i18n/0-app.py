#!/usr/bin/env python3
"""A simple flask app
"""


from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
# app.config.from_pyfile('mysettings.cfg')
# babel = Babel(app)


# define routes
@app.route('/')
def home():
    """"A default home route"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
