from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager
from app.config.keys import FLASK_SECRET_KEY

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["MONGODB_SETTINGS"] = {"db":"goodmusicdb", "host":"192.168.33.13"}
app.config['SECRET_KEY'] = FLASK_SECRET_KEY

db = MongoEngine(app)

# Manage Logins using flask-login extension
login_manager = LoginManager()
login_manager.init_app(app)

# app blueprints
def register_blueprints(app):
    # Prevents circular imports
    from app.search.views import mod as searchModule
    from app.users.views import mod as usersModule
    app.register_blueprint(searchModule)
    app.register_blueprint(usersModule)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
