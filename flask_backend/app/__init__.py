from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes import task_routes
    app.register_blueprint(task_routes)

    return app
