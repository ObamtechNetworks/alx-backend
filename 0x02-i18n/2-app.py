#!/usr/bin/env python3
"""A simple flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel


# Create a Config class to configure app languages and default settings
class Config:
    """Configures available languages, locale, and timezone"""
    LANGUAGES = ["en", "fr"]  # Supported languages
    BABEL_DEFAULT_LOCALE = "en"  # Default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Gets default locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# Define routes
@app.route('/')
def home():
    """A default home route"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
