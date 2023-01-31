import sqlite3
import pymongo
from flask import Flask, request
import random

app = Flask(__name__)


@app.route('/')
def hello_companies():
    return 'Companies'


@app.route('/get_companies', methods=["GET"])
def readDataSQLite():
    connect = sqlite3.connect(r"/home/visitor/Desktop/Realen-Proekt-Python/data.db")
    cursor = connect.cursor()
    sql = "select * from companies"
    cursor.execute(sql)
    results = cursor.fetchall()  # we can use fetchone(for one company), fetchall(for all companies) and fetchmany(
    # for how many companies we want)
    return results


def get_database():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    database = client["flaskapp"]
    return database


db = get_database()


@app.route('/create', methods=["POST"])
def create_companies():
    id = request.form.get("id")
    name = request.form.get("name")
    country_iso = request.form.get("country_iso")
    city = request.form.get("city")
    nace = request.form.get("nace")
    website = request.form.get("website")

    companies_collection = db["companies"]
    company = {
        "id": id,
        "name": name,
        "country_iso": country_iso,
        "city": city,
        "nace": nace,
        "website": website,
    }
    companies_collection.insert_one(company)
    return f"Successfully added company {name} - {country_iso} - {id}"


if __name__ == '__main__':
    port = 5000 + random.randint(0, 999)
    print(port)
    url = "http://127.0.0.1:{0}".format(port)
    print(url)
    app.run(use_reloader=False, debug=True, port=port)
