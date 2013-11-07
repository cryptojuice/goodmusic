from flask import Blueprint, request, render_template, flash, g, session,\
        redirect, url_for, jsonify

mod = Blueprint('users', __name__, url_prefix='/users')


@mod.route('/register', methods=['GET','POST'])
def register():
    pass

@mod.route('/login', methods=['POST'])
def login():
    pass

@mod.route('/logout', methods=['POST'])
def logout():
    pass

