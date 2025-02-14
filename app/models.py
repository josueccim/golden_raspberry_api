# -*- coding: iso-8859-1 -*-

from flask_sqlalchemy import SQLAlchemy

from app.database import db

class Movie(db.Model):
    """Modelo que representa um filme no banco de dados."""

    id          = db.Column(db.Integer,     primary_key=True,   index=True)
    title       = db.Column(db.String(255), nullable=False)
    year        = db.Column(db.Integer,     nullable=False,     index=True)
    studios     = db.Column(db.String(255), nullable=False)
    producer    = db.Column(db.String(255), nullable=False,     index=True)
    winner      = db.Column(db.Boolean,     default=False)

    def to_dict(self):
        """Converte a inst�ncia do modelo em um dicion�rio."""

        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'studios': self.studios,
            'producer': self.producer,
            'winner': self.winner
        }

    def __repr__(self):
        """Representa��o leg�vel do modelo Movie."""

        return f'<Movie {self.title}>'