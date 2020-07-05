import mysql.connector as ms
from mysql.connector import Error
from helper import Formatter
import os

class Mysql(object):
    def __init__(self):
        # enter your server IP address/domain name
        self.HOST = "sql9.freemysqlhosting.net"
        # database name, if you want just to connect to MySQL server, leave it empty
        self.DATABASE = "sql9352462"
        # this is the user you create
        self.USER = "sql9352462"
        # user password
        self.PASSWORD = "KRenv6IBFD"
        #DataBase Port
        self.PORT = '3306'
        try:
            self.connection = ms.connect(host=self.HOST,
                                                database=self.DATABASE,
                                                user=self.USER,
                                                password=self.PASSWORD)
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
        except Error as e:
            print("Error while connecting to MySQL", e)

    def execute_query(self,query):
        self.cursor.execute(query)
        record = self.cursor.fetchall()#Formatter.format_cursor(self.cursor.fetchall())
        return record

    def run_insert(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return 'Done'

    def build_query(self, query_file, *args):
        with open(
            os.path.join(
                os.path.abspath(
                    os.path.join(os.path.dirname(__file__), "..", "queries")
                ),
                query_file,
            ),
            "r",
            encoding="utf-8",
        ) as query:

            sql = query.read()
        sql = sql.format(*args)
        return sql