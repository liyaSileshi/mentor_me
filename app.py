from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/signup')
def sign_up():
    return 'signup'


@app.route('/signin')
def sign_in():
    return 'sign in'


if __name__ == '__main__':
    app.run(debug=True)

