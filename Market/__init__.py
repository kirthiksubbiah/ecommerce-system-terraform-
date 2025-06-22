from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect  # ✅ Add this
import os
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:admin123@database-1.cnas22u8mzr6.us-west-2.rds.amazonaws.com:3306/ecommerce"
app.config['SECRET_KEY'] = "my_super_secret_key_123456"
 
# ✅ Init extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
csrf = CSRFProtect(app)  # ✅ Enables CSRF protection for all WTForms
login_manager.login_view = 'LoginPage'
login_manager.login_message_category = 'info'
 
with app.app_context():
    db.create_all()
 
from Market import routes
