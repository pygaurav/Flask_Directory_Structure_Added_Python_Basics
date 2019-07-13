from flask import Flask
from flask_restful import Resource,Api
from flask_jwt import JWT


app = Flask(__name__)
api = Api(app)


from app import admin
from app import security
from app import components