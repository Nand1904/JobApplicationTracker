from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()  # Create database tables
        app.register_blueprint(routes.main)

    return app