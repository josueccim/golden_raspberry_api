# -*- coding: iso-8859-1 -*-

import csv

from flask import current_app
from app.database import db
from app.models import Movie

def load_data_from_csv(csv_file):
    
    with current_app.app_context():
        db.session.query(Movie).delete()
        db.session.commit()

        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')

            for row in reader:
                movie = Movie(
                    title       =   row['title'],
                    year        =   int(row['year']),
                    studios     =   row['studios'],
                    producer    =   row['producers'],
                    winner      =   row['winner'].strip().lower() == 'yes'
                )
                db.session.add(movie)

        db.session.commit()
