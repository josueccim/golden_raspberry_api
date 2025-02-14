# -*- coding: iso-8859-1 -*-
import pytest

from app import create_app
from app import db
from app.models import Movie


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

@pytest.fixture
def setup_data():
    movie1 = Movie(title='Movie1', year=2000, studios='Std 1', producer='Producer1', winner=True)
    movie2 = Movie(title='Movie2', year=2005, studios='Std 1', producer='Producer1', winner=True)
    movie3 = Movie(title='Movie3', year=1990, studios='Std 1', producer='Producer2', winner=True)
    movie4 = Movie(title='Movie4', year=2000, studios='Std 1', producer='Producer2', winner=True)
    movie5 = Movie(title='Movie5', year=2010, studios='Std 1', producer='Producer3', winner=True)
    movie6 = Movie(title='Movie6', year=2015, studios='Std 1', producer='Producer3', winner=True)
    db.session.add_all([movie1, movie2, movie3, movie4, movie5, movie6])
    db.session.commit()

def test_get_producer_intervals(client, setup_data):
    
    response = client.get('/producers/max-min-interval')
    assert response.status_code == 200

    data = response.get_json()
    expected_min = [
        {'producer': 'Producer1', 'interval': 5, 'previousWin': 2000, 'followingWin': 2005},
        {'producer': 'Producer3', 'interval': 5, 'previousWin': 2010, 'followingWin': 2015}
    ]
    expected_max = [
        {'producer': 'Producer2', 'interval': 10, 'previousWin': 1990, 'followingWin': 2000}
    ]

    assert 'max' in data and 'min' in data, "Resposta nao contem os intervalos esperados"
    assert len(data['min']) > 0 and len(data['max']) > 0
    assert isinstance(data['max'], list) and isinstance(data['min'], list), "Formato de resposta valido"

    print(data['min'])
    print(expected_min)
    assert data['min'] == expected_min, "Intervalos minimos nao correspondem"
    assert data['max'] == expected_max, "Intervalos maximos nao correspondem"
