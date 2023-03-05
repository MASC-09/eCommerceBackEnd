import functools
from flask import (jsonify,Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db


bp = Blueprint('games', __name__, url_prefix='/games')


'''Endpoint to get all the games saved it the database'''
@bp.route('/all', methods=['GET'])
def all_games():
    db = get_db()
    error = None

    all_games = db.execute('SELECT * FROM GAMES;').fetchall()
    
    if len(all_games) <= 0:
        error = 'There are no games stored in the data base.'
        return jsonify({'success': False, 'error': error}), 400

    games_list = []
    for game in all_games:
        game_data = {
            'gameID': game['gameID'],
            'name': game['name'],
            'description': game['description'],
            'price': game['price'],
            'image': game['image'],
            'genre': game['genre'],
            'developer': game['developer'],
            'avergeRating' : game['avergeRating']
        }
        games_list.append(game_data)
    flash(error)
    return jsonify({'games': games_list})

'''End point to get the top 6 rated games saved in the database.'''
@bp.route('/top', methods=['GET'])
def top_games():
    db = get_db()
    error = None

    top_games = db.execute('SELECT * FROM GAMES ORDER BY avergeRating DESC LIMIT 6;').fetchall()
    
    if len(top_games) <= 0:
        error = 'There are no games stored in the data base.'
        return jsonify({'success': False, 'error': error}), 400

    games_list = []
    for game in top_games:
        game_data = {
            'gameID': game['gameID'],
            'name': game['name'],
            'description': game['description'],
            'price': game['price'],
            'image': game['image'],
            'genre': game['genre'],
            'developer': game['developer'],
            'avergeRating' : game['avergeRating']
        }
        games_list.append(game_data)
    return jsonify({'top_games': games_list})


'''Method to get all the games from the desired genre coming from the GET request'''
@bp.route('/<string:genre>', methods=['GET'])
def games_by_genre(genre):
    # data = request.get_json()
    # genre = data['genre']

    db = get_db()
    error = None

    games_by_genre = db.execute(
        'SELECT * FROM GAMES WHERE genre = (SELECT genreID FROM GENRES WHERE name = ?)', (genre,)).fetchall()
    
    if len(games_by_genre) <= 0:
        error = f'There are no games of the genre \'{genre}\' stored in the data base.'
        return jsonify({'success': False, 'error': error}), 400

    games_list = []
    for game in games_by_genre:
        game_data = {
            'gameID': game['gameID'],
            'name': game['name'],
            'description': game['description'],
            'price': game['price'],
            'image': game['image'],
            'genre': game['genre'],
            'developer': game['developer'],
            'avergeRating' : game['avergeRating']
        }
        games_list.append(game_data)
    return jsonify({'games_by_genre': games_list})