"""This module defines all the paths for the user module"""
from app.models.message import Messages
from app.models.skills import Skills
from app.models.user_skills import UserSkills
from app.models.user import User
from app.models.education import Education
from app.models.userEducation import UserEducation
from app.models.experience import Experience
from app.models.userExperience import UserExperience

from app.models import storage
from app.views import app_views

from flask import jsonify, request, abort
from datetime import datetime, timedelta
from flasgger import Swagger, swag_from

# get a user's profile


@app_views.route('/user/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """

    Get users' profile
    ---
    tags:
      - Profile
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
      '404':
        description: Invalid input
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
    """

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


@app_views.route('/users/<user_id>/skills', methods=['POST'])
def add_user_skill(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    if 'SkillID' not in data or 'ProficiencyLevel' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if user and skill exist
    user = storage.get(User, user_id)
    skill = storage.get(Skills, data['SkillID'])
    user_skill = storage.all(UserSkills)
    for user_skill in user_skill.values():
        if user_skill.UserID == user_id and user_skill.SkillID == data['SkillID']:
            return jsonify({"error": "User already has this skill"}), 400
    print(user_skill)
    if not user or not skill:
        return jsonify({"error": "User or Skill not found"}), 404

    # Create new UserSkills instance
    user_skill = UserSkills(
        UserID=user_id, SkillID=data['SkillID'], ProficiencyLevel=data['ProficiencyLevel'])
    user_skill.save()
    return jsonify(user_skill.to_dict()), 201

#  DELETE /users/{userId}/skills/{skillId}: Remove a skill from user profile.UserSkills


@app_views.route('/users/<user_id>/skills/<skill_id>', methods=['DELETE'], strict_slashes=False)
def delete_user_skill(user_id, skill_id):
    """this function delete_user_skill"""
    user_skill = storage.get_obj(UserSkills, (user_id, skill_id))
    if not user_skill:
        return jsonify({"error": "UserSkill not found"}), 404
    user_skill.delete()
    return jsonify({"Success": f"UserSkill {user_skill.id} delete successfully"}), 201

# POST /users/{userId}/education: Add education details to user profile.


@app_views.route('/users/<user_id>/education', methods=['POST'], strict_slashes=False)
def add_education(user_id):
    """this function add_education"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'InstitutionName' not in data or 'Degree' not in data or 'FieldOfStudy' not in data or 'StartDate' not in data or 'EndDate' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    user = storage.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    education = Education(**data)
    user_education = UserEducation(UserID=user_id, EducationID=education.id)

    education.save()
    user_education.save()
    return jsonify(education.to_dict()), 201
# GET /users/{userId}/education: Get education details of a user.


@app_views.route('/users/<user_id>/education', methods=['GET'], strict_slashes=False)
def get_user_education(user_id):
    """this function get_user_education"""
    user = storage.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user_education = storage.all(UserEducation)
    return jsonify([education.to_dict() for education in user_education.values()]), 200
# POST /users/{userId}/experience: Add work experience to user profile.


@app_views.route('/users/<user_id>/experience', methods=['POST\
'], strict_slashes=False)
def add_experience(user_id):
    """this function add_experience"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'Company' not in data or 'Title' not in data or 'StartDate\
    ' not in data or 'EndDate' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    user = storage.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    experience = Experience(**data)
    user_experience = UserExperience(
        UserID=user_id, ExperienceID=experience.id)
    experience.save()
    user_experience.save()
    return jsonify(experience.to_dict()), 201


@app_views.route('/users/<user_id>/experience/<experience_id\
>', methods=['DELETE'], strict_slashes=False)
def delete_experience(user_id, experience_id):
    """this function delete_experience"""
    user_experience = None
    experience = storage.all(UserExperience)
    for experience in experience.values():
        if experience.UserID == user_id and experience.ExperienceID == experience_id:
            user_experience = experience
    if not user_experience:
        return jsonify({"error": "UserExperience not found"}), 404
    user_experience.delete()
    experience = storage.get(Experience, experience_id)
    experience.delete()
    return jsonify({"Success": f"UserExperience {user_experience.id}\
    delete successfully"}), 201

# GET /users/{userId}/notifications: Get notifications for a user.


def get_notifications(user_id):
    """this function get_notifications"""
    user = storage.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    messages = storage.all(Messages)
    # Get all messages for user
    messages = {k: v for k, v in messages.items() if v.UserID == user_id}
    return jsonify([message.to_dict() for message in messages.values()]), 200
