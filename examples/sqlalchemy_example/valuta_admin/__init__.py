from flask import Flask, request, session
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()

app: Flask


def get_locale():
    override = request.args.get("lang")

    if override:
        session["lang"] = override

    return session.get("lang", "en")


def create_app(config_filename: str) -> Flask:
    global app
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    db.init_app(app)

    return app


create_app("config.py")


# Initialize babel
babel = Babel(app, locale_selector=get_locale)


import valuta_admin.main
