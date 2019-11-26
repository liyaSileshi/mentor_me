from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy

from pymongo import MongoClient
from bson.objectid import ObjectId
import os
import json
from datetime import datetime
from pymongo import MongoClient

client = MongoClient()
db = client.MentorMe
mentors = db.mentors
mentee = db.mentors
app = Flask(__name__)

# m1={'Name':'Lorem', 'age':21}
m2= {'Name':'red', 'age':20}
mentee.insert_one(m2)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mentors')
def mentors_list():
    return render_template('mentors.html', mentors = mentors.find())

@app.route('/mentors/<mentor_id>')
def mentor_profile(mentor_id):
    mentor = mentors.find_one({'_id' : ObjectId(mentor_id)})
    return render_template('mentor_profile.html', mentor = mentor)

# @app.route('/books/<book_id>')
# def book_show(book_id):
#     """Show a single book."""
#     book = books.find_one({'_id' : ObjectId(book_id)})
#     book_users = users.find({'book_id': ObjectId(book_id)})
#     return render_template('book_show.html', book= book)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/signup')
def sign_up():
    return 'signup'

@app.route('/signin')
def sign_in():
    return 'sign in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)


