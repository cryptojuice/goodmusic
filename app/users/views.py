from flask import Blueprint, request, render_template, flash, g, session,\
        redirect, url_for, jsonify

mod = Blueprint('users',__name__, url_prefix('/users'))
