from flask import Flask
from flask_cors import CORS
from .routes import bp  # Note o ponto antes de routes
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def create_app():
    app = Flask(__name__,
               template_folder='../../frontend/templates',
               static_folder='../../frontend/static')
    CORS(app)
    app.register_blueprint(bp)
    return app