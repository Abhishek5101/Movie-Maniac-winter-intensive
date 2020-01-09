from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '567fbdf4643402c860b90b823a57df29'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	
	def __repr__(self):
		return f'{self.username}'


# cluster = MongoClient("mongodb+srv://abhi:%40AKak5101mongo@cluster0-dd95h.mongodb.net/test?retryWrites=true&w=majority")
# db = cluster["test"]
# collection = db["test"]


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


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', form=form)


