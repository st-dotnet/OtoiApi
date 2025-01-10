from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user import User

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/login", methods=["POST"])
def login():
    """
    Login a user
    ---
    tags:
      - Authentication
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
                example: "admin"
              password:
                type: string
                example: "admin123"
    responses:
      200:
        description: Successful login
        content:
          application/json:
            schema:
              type: object
              properties:
                access_token:
                  type: string
      401:
        description: Invalid credentials
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        token = create_access_token(identity={"username": user.username, "role": user.role.name})
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401
