## project/__init__py.py
from flask import Flask,render_template
from pymongo import MongoClient


app = Flask(__name__)
ap.config.from_pyfile('__config.py')
client = MongoClient('localhost:27017')
db = client.twitter

from project.api.views import api_blueprint

app.register_blueprint(api.blueprint)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404

