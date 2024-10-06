from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Bootstrap(app)
    db.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate

    # Initialize Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'  # Set the endpoint for login

    # User loader function for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.main)

    return app