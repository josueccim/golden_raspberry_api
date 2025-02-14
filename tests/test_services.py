# -*- coding: iso-8859-1 -*-

import pytest

from unittest.mock import patch
from app.services import get_producer_intervals
from app.models import Movie

@pytest.fixture
def mock_db_session():
    with patch('app.services.db.session.query') as mock_query:
        yield mock_query

def test_no_producers(mock_db_session):
    mock_db_session.return_value.filter_by.return_value.order_by.return_value.all.return_value = []
    result = get_producer_intervals()
    assert result == {'message': 'No data available'}

def test_single_producer_single_win(mock_db_session):
    mock_db_session.return_value.filter_by.return_value.order_by.return_value.all.return_value = [
        ('Producer1', 2000)
    ]
    result = get_producer_intervals()
    assert result == {'message': 'No data available'}

def test_multiple_producers_multiple_wins(mock_db_session):
    mock_db_session.return_value.filter_by.return_value.order_by.return_value.all.return_value = [
        ('Producer1', 2000),
        ('Producer1', 2005),
        ('Producer2', 1990),
        ('Producer2', 2000)
    ]
    result = get_producer_intervals()
    assert 'min' in result and 'max' in result
    assert len(result['min']) > 0 and len(result['max']) > 0

def test_multiple_producers_same_interval(mock_db_session):
    mock_db_session.return_value.filter_by.return_value.order_by.return_value.all.return_value = [
        ('Producer1', 2000),
        ('Producer1', 2005),
        ('Producer2', 2010),
        ('Producer2', 2015)
    ]
    result = get_producer_intervals()
    assert 'min' in result and 'max' in result
    assert len(result['min']) == 2 and len(result['max']) == 2
    assert result['min'][0]['interval'] == 5
    assert result['max'][0]['interval'] == 5