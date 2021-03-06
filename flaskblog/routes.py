from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User
from flask_login import login_user, current_user, logout_user, login_required
import requests
import json

TMDB_API_KEY = '23efb496361ed8a18ef9bc9238bf5c14'

"""
Home route to index page
"""
@app.route('/')
def home():
	return render_template('index.html')

"""
Register route takes in both GET and POST requests
if form in validated, user is added to the DB and redirected to Login page
if not, they are returned to same route with validation errors
"""
@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created! You are now able to log in', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

"""
Login Route authenticates the user and if it fails, returns back to self
with validation errors
"""
@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('show_movies'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login.html', title='Login', form=form)

"""
Logs the user out
"""
@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

"""
This route will be more useful later when creating user profiles
"""
@app.route("/account")
@login_required
def account():
	return render_template('account.html', title='Account')

"""
movies route has a default search query of word 'up'
you can change that by making your own searches though search bar
as a POST request which will again call the IMDB API
"""
@app.route("/movies", methods=['GET', 'POST'])
def show_movies():
	if request.method == 'POST':
		search_word = request.form.get('search')
	else:
		search_word = 'up'
	query_string = {
		'api_key': TMDB_API_KEY,
		'language': 'en-US',
		'query': search_word,
		'include_adult': 'False'
	}
	
	results = requests.get("https://api.themoviedb.org/3/search/multi?", query_string)
	movies = results.json()["results"]
	return render_template('movies.html', results=movies)
