from flask import Flask
from app import create_app
from app.seed import seed_data
from app.seed import seed_person_types
from app.extensions import db


app = create_app()

# Middleware to add CORS headers
# @app.after_request
# def add_cors_headers(response):
#     response.headers.add("Access-Control-Allow-Origin", "*")  # Allow all origins; restrict as needed
#     response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
#     response.headers.add("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
#     return response

# with app.app_context():
#     seed_person_types()

if __name__ == "__main__":
    app.run(port=5000)
