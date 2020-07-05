# encoding: utf-8

import flask_restful as restful
from flask import jsonify
from flask_restful import reqparse
from services import Mysql

class Cart(restful.Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("mode" , type=str)
        parser.add_argument("login", type=str)
        parser.add_argument("item" , type=str)
        parser.add_argument("price" , type=str)
        parser.add_argument("quantity" , type=str)
        args = parser.parse_args()
        ms = Mysql()
        if(args.mode == 'history'):
            query = ms.build_query('products.sql')
            results = ms.execute_query(query)
            return jsonify({
                "data": results
            })
        elif(args.mode == 'orders'):
            query = ms.build_query('orderProgress.sql',args.login)
            results = ms.execute_query(query)
            return jsonify({
                "data": results
            })
        elif(args.mode == 'insert'):
            query = ms.build_query('insertHistory.sql',args.login,args.item,args.price,args.quantity)
            results = ms.run_insert(query)
            return jsonify({
                    "data": results
                })
        elif(args.mode == 'clear'):
            query = ms.build_query('clearProgress.sql',args.login)
            results = ms.run_insert(query)
            return jsonify({
                    "data": results
                })

            

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str)
        parser.add_argument("item" , type=str)
        args = parser.parse_args()
        ms = Mysql()
        query = ms.build_query('addItem.sql',args.login,args.item.replace('%20',' '))
        results = ms.run_insert(query)
        return jsonify({
                "data": results
            })