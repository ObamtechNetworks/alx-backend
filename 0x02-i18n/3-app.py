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
    # Check if 'locale' is in the URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Fallback to the default locale if the 'locale' parameter is invalid or not present
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Define routes
@app.route('/')
def home():
    """A default home route"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
