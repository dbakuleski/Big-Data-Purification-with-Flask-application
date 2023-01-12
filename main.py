import sqlite3
import re
import cleanco
import pymongo
from flask import Flask
import requests
import random

app = Flask(__name__)


def readDataSQLite():
    connect = sqlite3.connect(r"/home/visitor/Desktop/Realen-Proekt-Python/data.db")
    cursor = connect.cursor()
    sql = "select * from companies"
    cursor.execute(sql)
    results = cursor.fetchmany(5) # we can use fetchone(for one company), fetchall(for all companies) and fetchmany(
    # for how many companies we want)
    print(results)


readDataSQLite()

if __name__ == '__main__':
    port = 5000 + random.randint(0, 999)
    print(port)
    url = "http://127.0.0.1:{0}".format(port)
    print(url)
    app.run(use_reloader=False, debug=True, port=port)
