#!/usr/bin/env python3
"""Flask app with Babel translations setup
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


# Create a Config class to configure app languages and default settings
class Config:
    """Configures available languages, locale, and timezone"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Create Flask app instance
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Select a language translation"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Define routes
@app.route('/')
def home():
    """A default home route"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
