"""This module defines all the paths for the user module"""
from app.models.skills import Skills
from app.models.user import User
from app.models import storage
from app.views import app_views
from flask import jsonify, request, abort
from datetime import datetime, timedelta


# add new Skills

@app_views.route("/skills", methods=["POST"], strict_slashes=False)
def add_post():
    """Add a new skill"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    skill = Skills(**data)
    print(skill)
    # check if the skill exists
    skill.save()

    return jsonify({"Success": "Skill added successfully"}), 201


# get all all Skills
@app_views.route("/skills", methods=["GET"], strict_slashes=False)
def get_skills():
    """This function gets all functions"""
    skills = storage.all(Skills)
    return jsonify([skill.to_dict() for skill in skills.values()])

# delete a Skill


@app_views.route("/skills/<skill_id>", methods=["DELETE"], strict_slashes=False)
def delete_skill(skill_id):
    """this function deletes a specific skill"""
    skill = storage.get(Skills, skill_id)
    if not skill:
        return jsonify({"error": "Skill not found"}), 404
    skill.delete()
    return jsonify({"Success": f"Skill {skill.id} delete successfully"}), 201
