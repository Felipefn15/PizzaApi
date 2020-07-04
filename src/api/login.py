# encoding: utf-8

import flask_restful as restful
from flask import jsonify
from flask_restful import reqparse
from services import Mysql

class Login(restful.Resource):

    def post(self):
       return 'Login'
