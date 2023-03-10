import functools
from flask import (jsonify,Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('cart', __name__, url_prefix='/cart')

'''Endpoint to get the user's games stored in the cart'''
@bp.route('/', methods=['GET'])
def games_in_cart():
    userID = session['userID']

    db = get_db()
    error = None
    
    if userID is None:
        error = 'You must be logged in to make this request.'
        return jsonify({'success': False, 'error': error}), 400
    
    if error is None:
        gamesInCart = db.execute('SELECT * FROM GAMES WHERE gameID IN (SELECT gameID FROM CARTS WHERE userID = ?);', (userID)).fetchall()
        # cartInfo = db.execute('SELECT * FROM CARTS WHERE userID = ?;', (userID)).fetchall()

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
                'genre': game['genre'],
                'developer': game['developer'],
                'avergeRating' : game['avergeRating']
            }

            games_list.append(game_data)
        
        return jsonify({'success': True, 'games_in_cart': games_list})


'''Endpoint to add a game to the user's cart'''
@bp.route('/add_game', methods=['POST'])
def add_game():
    data = request.get_json()
    gameID = data['gameID']
    userID = session['userID']

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

