from flask import Flask
from .views import main_blueprint
from .auth import auth_blueprint
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os


def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.getenv('FLASK_PASSWORD')
    
    jwt = JWTManager(app)
    
    # CORS(app, resources={r"/app/*": {"origins": "http://localhost:3000"}})
    CORS(app)
    app.config.from_pyfile('../config.py')
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    return app