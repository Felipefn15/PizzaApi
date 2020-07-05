# encoding: utf-8

import flask_restful as restful
from flask import jsonify
from flask_restful import reqparse
from services import Mysql

class Login(restful.Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str)
        parser.add_argument("password" , type=str)
        args = parser.parse_args()
        ms = Mysql()
        query = ms.build_query('login.sql',args.login,args.password)
        results = ms.execute_query(query)
        return jsonify({
             "data": results
        })