"""This module defines all the paths for the user module"""
from app.models.skills import Skills
from app.models.user import User
from app.models import storage
from app.views import app_views
from flask import jsonify, request, abort
from datetime import datetime, timedelta
from flasgger import Swagger, swag_from


# add a new skill to the system
@app_views.route("/skills", methods=["POST"], strict_slashes=False)
def post_skill():
    """Add a new skill to the system"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if "SkillName" not in data:
        return jsonify({"error": "Missing SkillName"}), 400
    new_skill = Skills(**data)
    new_skill.save()
    return jsonify(new_skill.to_dict()), 201

# get all skills


@app_views.route('/skills', methods=['GET'], strict_slashes=False)
def get_skills():
    """Get all skills"""
    skills = storage.all(Skills)
    skills = [skill.to_dict() for skill in skills.values()]
    return jsonify(skills), 200

# delete skill


@app_views.route('/skills/<skill_id>', methods=["DELETE"], strict_slashes=False)
def delete_skill(skill_id):
    """this function deletes skill"""
    skill = storage.get(Skills, skill_id)
    if not skill:
        return jsonify({"error": "Skill not found"}), 404
    skill.delete()
    return jsonify({"Sucess": f"skill {skill.SkillName} deleted"})
