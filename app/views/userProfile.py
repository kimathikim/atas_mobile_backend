"""This module defines all the paths for the user module"""
from app.models.skills import Skills
from app.models.user import User
from app.models import storage
from app.views import app_views
from flask import jsonify, request, abort
from datetime import datetime, timedelta
from flasgger import Swagger, swag_from

# get a user's profile


@app_views.route('/user/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Get a user's profile"""

    print(user_id)
    if not user_id:
        return jsonify({"error": "User id not added"}), 400
    user = storage.get(User, user_id)
    print(user)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

# PUT /users/{userId}: Update user profile details


@app_views.route('/user/<user_id>', methods=['PUT'], strict_slashes=False)
def update_profile(user_id):
    """this method updates a user profile"""
    data = request.get_json()
    user = storage.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    for key, value in data.items():
        setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200

# DELETE /users/{userId}: Delete a user account.


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """this function delete_user"""
    user = storage.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.delete()
    return jsonify({"Success": f"User {user.id} delete successfully"}), 201

# POST /users/{userId}/skills: Add a new skill to user profile


@app_views.route('/users/<user_id>/skills', methods=['POST'], strict_slashes=False)
def user_skills(user_id):
    """this function add a new skill to user profile"""
    data = request.get_json()
    user = storage.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    if not data:
        return jsonify({"error": "Skill not found"}), 404
    skill = Skills(**data)
    skill.user_id = user.id
    skill.save()
    return jsonify(skill.to_dict()), 201
