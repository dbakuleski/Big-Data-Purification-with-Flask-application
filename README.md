# Big Data Purification with Flask application

Welcome to the Big Data Purification application!

The Big Data Purification application is a Flask application that connects to a local SQLite database, gets the data (Company Names), cleans the data 
and writes the processed data in MongoDB.

The Big Data Purification comprises two parts:

* **App** - A Flask application that is hosted on local server
The Flask application has two API functions. One function reads from the local SQLite database and has only GET method. The other
function writes in MongoDB and has only POST method.
* **Names** - A script that makes calls to the API functions from the Flask application and process the company names

## Python packages you will need to run the application

The Big Data Purification uses the following python modules:

* sqlite3
* re
* cleanco 2.1
* pymongo 4.3.3
* flask 2.2.2
* requests

## Instructions to run the application

* Run App.py
* Run Names.py
* Use the MongoDB Compass application to view the database and the collection with processed data

