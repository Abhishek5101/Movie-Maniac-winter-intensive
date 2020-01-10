from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '567fbdf4643402c860b90b823a57df29'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['DATABASE_URL'] = 'postgres://sxeyeqbbivckfk:013bbfe40cc1d4083ed02566545c15925d1eef213a5d3d127688bb4c4a11fd7f@ec2-174-129-254-217.compute-1.amazonaws.com:5432/d124j9q9lhsfbk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
