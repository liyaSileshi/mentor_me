from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
import json
from datetime import datetime
from pymongo import MongoClient
from forms import RegistrationForm, LoginForm
import sys
#export secret_key='412eb254393c7dec141e79faf17b8a17'
host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/MentorMe')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
mentors = db.mentors
# mentee = db.mentee
users = db.users


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['secret_key']

class user(object):
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def json(self):
        return {
            'username': self.username,
            'password': self.password,
            'email': self.email
        }

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/mentors')
def mentors_list():
    #  mentor = {
    #     'name': "Bob",

    # }
    return render_template('mentors.html', mentors = mentors.find())

@app.route('/mentors/<mentor_id>')
def mentor_profile(mentor_id):
    mentor = mentors.find_one({'_id' : ObjectId(mentor_id)})
    # mentor = {
    #     'name': "Bob",
    # }
    return render_template('mentor_profile.html', mentor = mentor)

@app.route('/mentor_form')
def mentor_form():
    return render_template('mentor_form.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration page for users"""
    if request.method == 'POST':
        form = RegistrationForm()
        if form.validate_on_submit():
            if users.find_one({'username':form.username.data}):
                flash(f'Sorry, an account with this username already exists!')
                return redirect(url_for('register'))
            else:
                current_user = users.insert_one(user(form.username.data, form.password.data, form.email.data).json())
                flash(f'Congrats! You have successfully created an account!')
                return redirect(url_for('login'))
        else:
            flash(f'Incorrect credintials')
            return render_template('register.html',title='Register', form=form)

    if request.method == 'GET':
        form = RegistrationForm()
        return render_template('register.html', title = 'Register', form=form)

@app.route('/', methods=['GET', 'POST'])
def login():
    """ Users login page"""
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if users.find_one({'email': form.email.data}):
                if (form.email.data == users.find_one({"email": form.email.data})["email"]) and (form.password.data == users.find_one({"email": form.email.data})["password"]):
                    return redirect(url_for('index'))
                else:
                    flash(f"Login unsuccessful. Please check if email and password was correct", 'danger')
    return render_template('login.html', title='Login', form=form)
    
if __name__ == '__main__':
    app.run(debug=True)
