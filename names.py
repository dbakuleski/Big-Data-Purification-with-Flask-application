from flask import Flask, request
import sqlite3
import random
import re

app = Flask(__name__)
connect = sqlite3.connect(r"/home/visitor/Desktop/Realen-Proekt-Python/data.db")
cursor = connect.cursor()


@app.route("/one_company", methods=["GET"])
def readOneCompany():
    sql = "select * from companies"
    cursor.execute(sql)
    results = cursor.fetchone()
    return results


query = "select name from companies"
names = cursor.execute(query).fetchall()

cleaned_names = []
for name in names:
    name = name.strip()
    name = name.replace(" ", "")
    name = re.sub(r"[^a-zA-Z0-9]+", "", name)
    cleaned_names.append(name)

if __name__ == '__main__':
    port = 5000 + random.randint(0, 999)
    print(port)
    url = "http://127.0.0.1:{0}".format(port)
    print(url)
    app.run(use_reloader=False, debug=True, port=port)
