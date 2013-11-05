from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "Hello from flask."

# app blueprints
from app.search.views import mod as searchModule
app.register_blueprint(searchModule)
