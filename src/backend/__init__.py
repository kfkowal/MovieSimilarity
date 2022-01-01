
import os
from flask import Flask
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app)
    app.config['JSON_AS_ASCII'] = False
    with app.app_context():
        from .presentation import model_to2dController
        app.register_blueprint(model_to2dController.bp)
        return app