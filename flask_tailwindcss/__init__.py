"""Top-level package for Flask with Tailwindcss."""

__author__ = """Pyunghyuk Yoo"""
__email__ = "pyunghyuk@likelion.net"
__version__ = "0.1.0"

from flask import Flask, render_template

from flask_tailwindcss.config import config


def create_app(config_name):
    app = Flask(__name__)
    app_config = config.get(config_name)
    app.config.from_object(app_config)
    app_config.init_app(app)

    init_bp(app)

    return app


def init_bp(app):
    @app.route("/")
    def index():
        return render_template("index.html")
