from flask import Flask
from app.extensions import db, migrate, jwt
from app.routes import register_blueprints
from flasgger import Swagger
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    
    # CORS
    CORS(app)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Initialize Swagger
    swagger = Swagger(app)

    # Register blueprints
    register_blueprints(app)
    
    return app
