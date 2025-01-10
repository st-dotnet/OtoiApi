from flask import Blueprint
from app.routes.auth import auth_blueprint
from app.routes.user import user_blueprint
from app.routes.person import person_blueprint

def register_blueprints(app):
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(user_blueprint, url_prefix="/user")
    app.register_blueprint(person_blueprint, url_prefix="/persons")
