# encoding: utf-8

import flask_restful as restful
from flask import jsonify
from services import Mysql

class Itens(restful.Resource):

    def get(self):
        ms = Mysql()
        query = ms.build_query('products.sql')
        results = ms.execute_query(query)
        return jsonify({
             "data": results
        })
