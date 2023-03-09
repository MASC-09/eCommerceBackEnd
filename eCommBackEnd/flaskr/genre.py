import functools
from flask import (jsonify,Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db


bp = Blueprint('genre', __name__, url_prefix='/genre')


'''Endpoint to get all the genres saved it the database'''
@bp.route('/all', methods=['GET'])
def all_genres():
    db = get_db()
    error = None

    all_genres = db.execute('SELECT * FROM GENRES;').fetchall()
    
    if len(all_genres) <= 0:
        error = 'There are no genres stored in the data base.'
        return jsonify({'success': False, 'error': error}), 400

    genre_list = []
    for genre in all_genres:
        genre_data = {
            'genreID': genre['genreID'],
            'name': genre['name'],
            }
        genre_list.append(genre_data)
    flash(error)
    return jsonify({'genres': genre_list})
