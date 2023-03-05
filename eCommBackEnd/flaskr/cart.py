import functools
from flask import (jsonify,Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('cart', __name__, url_prefix='/cart')

'''Endpoint to get the user's cart'''
@bp.route('/', methods=['GET'])
def cart():
    data = request.get_json()
    userID = data['userID']

    db = get_db()
    error = None
    
    if userID is None:
        error = 'No user id detected.'
    
    if error is None:
        gamesInCart = db.execute('SELECT * FROM GAMES WHERE gameID IN (SELECT gameID FROM CARTS WHERE userID = ?);', (userID)).fetchall()
        cartInfo = db.execute('SELECT * FROM CARTS WHERE userID = ?;', (userID)).fetchall()

        if len(gamesInCart) <= 0:
            error = 'The cart is empty.'
            return jsonify({'success': False, 'error': error}), 400
        
        games_list = []
        for game in gamesInCart:
            game_data = {
                'gameID': game['gameID'],
                'name': game['name'],
                'description': game['description'],
                'price': game['price'],
                'image': game['image'],
                'genre': game['genre']
            }

            games_list.append(game_data)
        

    else:
        return jsonify({'success': False, 'error': error}), 400


    data = request.get_json()
    userID = data['userID']

    db = get_db()
    error = None

    cart = db.execute('SELECT gamesID FROM GAMES;').fetchall()
    
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
            'genre': game['genre']
        }
        games_list.apped(game_data)
    flash(error)
    return jsonify({'games': games_list})

'''Endpoint to add a game to the user's cart'''
@bp.route('/add_game', methods=['POST'])
def add_game():
    data = request.get_json()
    gameID = data['gameID']
    userID = data['userID']

    db = get_db()
    error = None

    if gameID is None:
        error = 'No game selected to add.'
    
    elif userID is None:
        error = 'No user id detected.'

    ###
    

'''Endpoint to remove a game from the user's cart'''
@bp.route('/remove_game', methods=['POST'])
def remove_game():
    data = request.get_json()
    gameID = data['gameID']

    db = get_db()
    error = None


    return None

