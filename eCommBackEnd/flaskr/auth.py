import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    data = request.get_json()
    name = data['name']
    password = data['password']
    email = data['email']
    address = data['address']

    db = get_db()
    error = None

    if not name:
        error = 'Name is required.'
    elif not password:
        error = 'Password is required.'
    elif not email:
        error = 'Email is required.'
    elif not address:
        error = 'Address is required.'
    
    if error is None:
        try:
            db.execute(
                "INSERT INTO USERS (name, password,email, address) VALUES (?, ?, ?, ?)",
                (name, generate_password_hash(password),email, address),
            )
            db.commit()
        except db.IntegrityError:
            error = f"Email {email} is already registered."
        else:
            return jsonify({'success':True})
    return  jsonify({'success': False, 'error': error}), 400

@bp.route('/login', methods=('GET', 'POST'))
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    db = get_db()
    error = None

    user = db.execute('SELECT * FROM USERS WHERE email = ?', (email)).fetchone()

    if user is None:
        error = 'No user found.'
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password.'
    
    if error is None:
        session.clear()
        session['user_id'] = user['userID']
        return jsonify({'success': True})
    else:
        return  jsonify({'success': False, 'error': error}), 400

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM USERS WHERE userID = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return jsonify({'success': True})


#view to make login necessary to make accions.
# def login_requiered(view):
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for('auth.login'))
#         return view(**kwargs)
    
#     return wrapped_view