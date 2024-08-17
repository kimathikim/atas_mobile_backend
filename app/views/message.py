"""This module defines all the paths for the user module"""
from app.models.skills import Skills
from app.models.user_skills import UserSkills
from app.models.user import User
from app.models.education import Education
from app.models.userEducation import UserEducation
from app.models.experience import Experience
from app.models.userExperience import UserExperience
from app.models.message import Messages

from app.models import storage
from app.views import app_views

from flask import jsonify, request, abort
from datetime import datetime, timedelta


@app_views.route('/messages', methods=['POST\
'], strict_slashes=False)
def add_message():
    """Add a message"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'SenderID' not in data or 'RecipientID' not in data or 'Content\
    ' not in data or 'IsRead' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    message = Messages(**data)
    message.save()
    return jsonify(message.to_dict()), 201

# GET /messages/{messageId}: Get details of a specific message.


@app_views.route('/messages/<message_id>', methods=['GET\
'], strict_slashes=False)
def get_message(message_id):
    """Get a message"""
    message = storage.get(Messages, message_id)
    if not message:
        return jsonify({"error": "Message not found"}), 404
    return jsonify(message.to_dict()), 200


@app_views.route('/messages/<message_id>', methods=['DELETE\
'], strict_slashes=False)
def delete_message(message_id):
    """Delete a message"""
    message = storage.get(Messages, message_id)
    if not message:
        return jsonify({"error": "Message not found"}), 404
    storage.delete(message)
    storage.save()
    return jsonify({}), 200
