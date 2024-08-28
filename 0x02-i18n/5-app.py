#!/usr/bin/env python3
"""Flask app with Babel translations and mock login setup
"""

from flask import Flask, render_template, request, g
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

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Retrieve user based on login_as parameter"""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """Set the global user based on the login_as parameter"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Select a language translation based on the request"""
    if g.user and g.user.get('locale'):
        return g.user['locale']
    return request.args.get('locale', request.accept_languages.best_match(
        app.config['LANGUAGES']))


# Define routes
@app.route('/')
def home():
    """A default home route"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
