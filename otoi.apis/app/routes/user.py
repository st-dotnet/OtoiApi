from flask import Blueprint, jsonify
from app.utils.decorators import role_required

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/profile", methods=["GET"])
@role_required(["Admin", "User"])
def profile():
    """
    Get user profile
    ---
    tags:
      - User
    security:
      - BearerAuth: []
    responses:
      200:
        description: User profile data
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "User profile data"
      403:
        description: Unauthorized
    """
    return jsonify({"message": "User profile data"}), 200
