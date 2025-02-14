# -*- coding: iso-8859-1 -*-

from app.models import db
from app.models import Movie

def get_producer_intervals():
    query = db.session.query(Movie.producer, Movie.year).filter_by(winner=True).order_by(Movie.producer, Movie.year).all()
    
    producers = {}
    intervals = []

    # Criar lista de produtores e anos
    for producer, year in query:

        if producer not in producers:
            producers[producer] = []

        producers[producer].append(year)
    
    for producer, years in producers.items():

        if len(years) > 1:
            sorted_years = sorted(years)

            for i in range(len(sorted_years) - 1):
                intervals.append({
                    'producer': producer,
                    'interval': sorted_years[i + 1] - sorted_years[i],
                    'previousWin': sorted_years[i],
                    'followingWin': sorted_years[i + 1]
                })
    
    if not intervals:
        return {'message': 'No data available'}

    max_interval = max(intervals, key=lambda x: x['interval']).get('interval')
    min_interval = min(intervals, key=lambda x: x['interval']).get('interval')

    # Monta as lista de retorno
    min_interval_list = [x for x in intervals if x['interval'] == min_interval]
    max_interval_list = [x for x in intervals if x['interval'] == max_interval]
    
    return {'min': min_interval_list, 'max': max_interval_list}