from flask import Flask
from .views import main_blueprint
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    # CORS(app, resources={r"/app/*": {"origins": "http://localhost:3000"}})
    CORS(app)
    app.config.from_pyfile('../config.py')
    app.register_blueprint(main_blueprint)
    return app