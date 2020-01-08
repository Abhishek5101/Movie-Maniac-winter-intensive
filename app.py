from flask import Flask, render_template, url_for
from pymongo import MongoClient
import requests
from bson.objectid import ObjectId


app = Flask(__name__)

cluster = MongoClient("mongodb+srv://abhi:%40AKak5101mongo@cluster0-dd95h.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]


@app.route('/')
def hello_world():
	return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)
