# -*- coding: iso-8859-1 -*-

from flask import Blueprint
from flask import jsonify
from flask import request

from app.database import db
from app.models import Movie
from app.services import get_producer_intervals

main_bp = Blueprint('main', __name__)

@main_bp.route('/producers/max-min-interval', methods=['GET'])
def producer_intervals():
    """Rota para obter os intervalos máximos e mínimos dos produtores."""

    result = get_producer_intervals()
    return jsonify(result)

@main_bp.route('/movies', methods=['GET'])
def get_movies():
    """Rota para obter a lista de filmes."""

    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies])

@main_bp.route('/movies', methods=['POST'])
def add_movie():
    """Rota para adicionar um novo filme."""

    data = request.get_json()

    new_movie = Movie(
        title = data['title'],
        year = data['year'],
        studios = data['studios'],
        producer = data['producer'],
        winner = data['winner']
    )

    db.session.add(new_movie)
    db.session.commit()
    return jsonify(new_movie.to_dict()), 201

@main_bp.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    """Rota para obter um filme específico pelo ID."""

    movie = Movie.query.get_or_404(id)
    return jsonify(movie.to_dict())