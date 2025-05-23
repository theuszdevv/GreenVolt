from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
import psycopg2

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'a5881f26bae925d752a97795'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:PML1RRjpQ8foE5y1@proudly-unbiased-spadefish.data-1.use1.tembo.io:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    login_manager.login_view = "page_login"
    login_manager.login_message = "Por favor, realize o login"
    login_manager.login_message_category = "info"

    from greenvolt import routes  # importa aqui dentro da função
    return app
