"""Top-level package for Flask with Tailwindcss."""

__author__ = """Pyunghyuk Yoo"""
__email__ = "pyunghyuk@likelion.net"
__version__ = "0.1.0"

from flask import Flask, render_template
from flask_assets import Bundle

from flask_tailwindcss.config import config
from flask_tailwindcss.extensions import assets


def create_app(config_name):
    app = Flask(__name__)
    app_config = config.get(config_name)
    app.config.from_object(app_config)
    app_config.init_app(app)

    init_assets(app)
    init_bp(app)

    return app


def init_assets(app):
    assets.init_app(app)
    css_all = Bundle("src/css/*.css", filters="postcss", output="dist/css/main.css")
    js_base = Bundle("src/js/alpine.js", output="dist/js/base.js")

    assets.register("css_all", css_all)
    assets.register("js_base", js_base)


def init_bp(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/alpine")
    def alpine():
        return render_template("alpine.html")
