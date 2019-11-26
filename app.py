from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from datetime import datetime
from pymongo import MongoClient

client = MongoClient()
db = client.MentorMe
mentors = db.mentors
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mentors')
def mentors_list():
    return render_template('mentors.html', mentors = mentors.find())

@app.route('/mentor_profile')
def mentor_profile():
    return render_template('mentor_profile.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/signup')
def sign_up():
    return 'signup'

@app.route('/signin')
def sign_in():
    return 'sign in'

if __name__ == '__main__':
    app.run(debug=True)


