import sqlite3
import pymongo
import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_companies():
    return 'Companies'


@app.route('/get-companies-names', methods=["GET"])
def readDataSQLite():
    connect = sqlite3.connect(r"/home/visitor/Desktop/Realen-Proekt-Python/data.db")
    cursor = connect.cursor()
    sql = "select * from companies"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


@app.route('/one-company-data', methods=["GET"])
def oneCompany():
    # http://localhost:5432/one-company-data?name="Name of the company"
    connect = sqlite3.connect(r"/home/visitor/Desktop/Realen-Proekt-Python/data.db")
    cursor = connect.cursor()
    company_name = request.args.get('name')
    sql = f"select * from companies where name == '{company_name}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return [result]


def get_database():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    database = client["flaskapp"]
    return database


db = get_database()


@app.route('/create', methods=["POST"])
def create_companies():
    data = json.loads(request.data)

    id = data.get("id")
    name = data.get("name")
    country_iso = data.get("country_iso")
    city = data.get("city")
    nace = data.get("nace")
    website = data.get("website")

    companies_collection = db["companies"]
    company_dictionary = {name: {
        "id": id,
        "country_iso": country_iso,
        "city": city,
        "nace": nace,
        "website": website,
    }
    }
    companies_collection.insert_one(company_dictionary)
    print("hello")
    return f"Successfully added company {name} - {country_iso} - {id}"


if __name__ == '__main__':
    port = 5769
    print(port)
    url = "http://127.0.0.1:{0}".format(port)
    print(url)
    app.run(use_reloader=False, debug=True, port=port)
