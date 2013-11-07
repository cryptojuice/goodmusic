from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

# app blueprints
from app.search.views import mod as searchModule
app.register_blueprint(searchModule)

from app.users.views ipmort mod as usersModule
app.register_blueprint(usersModule)
