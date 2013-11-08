from flask import Flask
from flask.ext.login import LoginManager
from app.config.keys import FLASK_SECRET_KEY

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = FLASK_SECRET_KEY

# Manage Logins using flask-login extension
login_manager = LoginManager()
login_manager.init_app(app)

# app blueprints
from app.search.views import mod as searchModule
app.register_blueprint(searchModule)

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)
