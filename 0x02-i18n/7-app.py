#!/usr/bin/env python3
"""Flask app with Babel translations and user timezone settings
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError


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
    """Set the global user and timezone"""
    g.user = get_user()
    g.timezone = get_timezone()


@babel.localeselector
def get_locale():
    """Select a language translation based on priority"""
    # Locale from URL parameter
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # Locale from request headers
    if request.accept_languages.best_match(app.config['LANGUAGES']):
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """Select a time zone based on priority and validate it"""
    # Timezone from URL parameter
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)  # Validate the timezone
            return timezone
        except UnknownTimeZoneError:
            pass

    # Timezone from user settings
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user['timezone'])  # Validate the timezone
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass

    # Default timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']


# Define routes
@app.route('/')
def home():
    """A default home route"""
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(debug=True)
