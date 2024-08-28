#!/usr/bin/env python3
"""A simple flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Instantiate Babel with the Flask app
babel = Babel(app)


# Create a Config class to configure app languages and default settings
class Config:
    """Configures available languages, locale, and timezone"""
    LANGUAGES = ["en", "fr"]  # Supported languages
    BABEL_DEFAULT_LOCALE = "en"  # Default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


# Apply the Config class to the app's configuration
app.config.from_object(Config)


# Define routes
@app.route('/')
def home():
    """A default home route"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
