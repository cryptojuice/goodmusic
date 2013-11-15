from flask import Blueprint, request, render_template, flash, g, session,\
        redirect, url_for, jsonify, Response
from flask.ext.login import current_user, login_required, logout_user
from flask.ext.scrypt import generate_password_hash, generate_random_salt, \
        check_password_hash
from app.users.models import User
from app import login_manager
from bson import ObjectId, json_util


mod = Blueprint('users', __name__, url_prefix='/api/v1/users')

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()

@mod.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.objects(id=session['user_id']).first()

@mod.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password'].encode('utf8')
    salt = generate_random_salt()
    password_hash = generate_password_hash(password, salt)

    # Check if email already exist in database
    # if account does not exist create account in database

    if User.objects(email=email).first() == None:
        user = User(email=email)
        user.accounts['internal'] = {"username":username, "password_hash":password_hash, \
                "salt":salt}
        user.save()
        ret = json_util.dumps({"message":"account created", "status":"success"})
        resp = Response(response=ret,
                        status=201,
                        mimetype="application/json")
        return resp
    else:
        ret = json_util.dumps({"message":"Email already exist in database"})
        resp = Response(response=ret,
                        status=200,
                        mimetype="application/json")
        return resp

@mod.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = User.objects(email=email).first()
    if user is not None:
        password_hash = user.accounts['internal']['password_hash']
        salt = user.accounts['internal']['salt']
        if check_password_hash(password, password_hash, salt):
            session['user_id'] = user.get_id()
            ret = json_util.dumps({"username":user.accounts['internal']['username']})
            resp = Response(response=ret, status=200, mimetype="application/json")
            return resp
    ret = json_util.dumps({"message":"Incorrect Username or Password."})
    resp = Response(response=ret, status=401, mimetype="application/json")
    return resp

@mod.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    print current_user.email
    logout_user()
    return "Bye!!!"
