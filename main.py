# -*- coding: iso-8859-1 -*-

import os

from app import create_app

from app.database import db
from app.models import Movie
from app.services import get_producer_intervals
from app.utils import load_data_from_csv

app = create_app()

with app.app_context():
    db.create_all()

    if os.path.exists('Movielist.csv'):
        load_data_from_csv('Movielist.csv')

if __name__ == '__main__':
    app.run(debug=True)