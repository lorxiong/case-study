import json
import request
from flask import Flask, redirect, url_for, request, render_template, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mydatabase'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello_user(name):
    return 'Hello ' + name + '!'

@app.route("/products/<int:product_id>", methods=["GET", "POST"])
def get_product(product_id):
    prod_id = mongo.db.collection.find_one({"id": product_id})
    if request.method == 'POST':
        new_price = '14.99'
        query = mongo.db.collection.find_one({'current_price': {'currency_code': 'USD', 'value': 13.49}})
        mongo.db.collection.update_one(query, new_price)
    elif request.method == 'GET':
        return product_id
    else:
        return "Product id not found"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
