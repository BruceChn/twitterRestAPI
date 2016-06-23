##project/api/views.py

from flask import flash,redirect,jsonify,session,url_for,Blurprint,make_response
from project import db


###config###

api_blueprint = Blueprint('api',__name__)

