"""This module defines all the paths for the user module"""

from app.models.user import User
from app.models import storage
from app.views import app_views
from flask import jsonify, request, abort
from datetime import datetime, timedelta
from flasgger import Swagger, swag_from


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


@app_views.route('/users/login', methods=['POST'], strict_slashes=False)
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
    responses:
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


@app_views.route('/users', methods=['GET'], strict_slashes=False)
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
    users = storage.all(User)
    users = [user.to_dict() for user in users.values()]
    return jsonify(users)
