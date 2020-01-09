from flask import Flask, render_template, url_for, flash, redirect
from pymongo import MongoClient
import requests
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '567fbdf4643402c860b90b823a57df29'

cluster = MongoClient("mongodb+srv://abhi:%40AKak5101mongo@cluster0-dd95h.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', form=form)


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', form=form)


if __name__ == "__main__":
	app.run(debug=True)
0