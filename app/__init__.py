from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    
    from .routes import main
    app.register_blueprint(main)

    return app