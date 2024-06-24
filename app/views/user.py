"""This module defines all the paths for the user moijdule"""
import jwt
from app.models.user import User
from app.models import storage
from app.views import app_views
from flask import jsonify, request, abort, session
from datetime import datetime, timedelta
from flasgger import Swagger, swag_from
from functools import wraps
import os
from flask import current_app


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        secret_key = current_app.config['SECRET_KEY']

        print(token)
        if not token:
            return jsonify({"error": "Token is missing"}), 401
        try:
            data = jwt.decode(token, secret_key, algorithms=["HS256"])
            print(data)
            session.setdefault('logged_in', True)
        except:
            return jsonify({"error": "Token is invalid"}), 401
        return f(*args, **kwargs)  # Add this line
    return decorated


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """

    Create a new user
    ---
    tags:
      - Users
    summary: Create a new user
    requestBody:
      description: User object that needs to be added
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/User'
    responses:
      '201':
        description: User created
        content:
          application/json:
            schema:
      '400':
        description: Invalid input
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
    """
    required_fields = ['email', 'password', 'first_name', 'last_name']
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400

    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201

# user login


@app_views.route('/login', methods=['POST'], strict_slashes=False)
def user_login():
    """
    User Login
    ---
    tags:
      - Users
    summary: User Login
    requestBody:
      description: User object that needs to be added
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/User'
 a   responses:
        201:
            description: User logged in
            content:
                application/json:
                    schema:
                type: object
                properties:
                    token:
                        type: string
        400:
            description: Invalid input
            content:
            application/json:
                schema:
                type: object
                properties:
                    error:
                    type: string
    """

    secret_key = current_app.config['SECRET_KEY']
    required_fields = ['email', 'password']
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing {', '.join(missing_fields)}"}), 400

    email, password = data['email'], data['password']
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    user = storage.get_by_email(User, email)
    if not user or password != user.password:
        return jsonify({"error": "User not found or Invalid password"}), 400
    print(user.to_dict())
    token_payload = {
        "user_name": user.first_name,
        'email': email,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    token = jwt.encode(token_payload, secret_key)
    if token:
        session['logged_in'] = True
        return jsonify({"token": token})
    return jsonify({"error": "Error generating token"}), 500


@ app_views.route('/users', methods=['GET'], strict_slashes=False)
@ token_required
def get_users():
    """
    Get all users
    ---
    tags:
      - Users
    operations:
      - httpMethod: GET
        summary: Retrieve all users
        responses:
          '200':
            description: List of all users
            content:
              application/json:
                schema:
                  type: array
                  items:
                    $ref: '#/components/schemas/User'
    """
    if session.get('logged_in') is None or not session['logged_in']:
        return jsonify({"error": "Unauthorized"}), 401

    users = storage.all(User)
    users = [user.to_dict() for user in users.values()]
    return jsonify(users), 200
