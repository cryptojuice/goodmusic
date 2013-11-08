from flask import Blueprint, request, render_template, flash, g, session,\
        redirect, url_for, jsonify, Response
from flask.ext.login import current_user, login_required, logout_user
from app.users.forms import RegistrationForm
from app.users.models import User
from app import login_manager
from app.config.database import db
from bson import ObjectId, json_util
from os import urandom
import scrypt, base64


mod = Blueprint('users', __name__, url_prefix='/api/1.0/users')

@login_manager.user_loader
def load_user(userid):
    user = User(ObjectId(userid))
    return user

@mod.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = db.users.find_one({"_id":ObjectId(session['user_id'])})

def generate_password_hash(password):
    password = password.encode('utf8')
    pw_salt = base64.b64encode(urandom(64))
    pw_hash = base64.b64encode(scrypt.hash(password, pw_salt))
    return pw_hash, pw_salt

def verify_password(email, password):
    user = db.users.find_one({"email":email})
    if user['pw_hash'] == base64.b64encode(scrypt.hash(password.encode('utf8'), user['pw_salt'].encode('utf8'))):
        return True
    return False

@mod.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password'].encode('utf8')
    pw_hash, pw_salt = generate_password_hash(password)

    if db.users.find_one({"email":email}) is None:
        user = {"email":email, "username":username, "pw_hash":pw_hash, "pw_salt":pw_salt}
        session['user_id'] = str(db.users.insert(user))
        ret = json_util.dumps(db.users.find_one(user)['_id'])
        resp = Response(response=ret,
                        status=200,
                        mimetype="application/json")
        return resp
    else:
        return "Email address {0} already has an account.".format(email)

@mod.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = db.users.find_one({"email":email})
    if verify_password(email, password):
        session['user_id'] = str(user['_id'])
        return redirect("/index.html")
    return "Incorrect e-mail or password."

@mod.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    print session['user_id']
    logout_user()
    return "Bye!!!"
