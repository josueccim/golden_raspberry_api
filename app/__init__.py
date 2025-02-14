# -*- coding: iso-8859-1 -*-

from flask import Flask

from app.database import db
from app.models import Movie
from app.routes import main_bp

def create_app():
    """Cria e configura a aplicação Flask."""

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(main_bp)

    return app
