from flask import Blueprint
from functools import wraps
from flask import session, current_app, request, jsonify
import jwt


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1/")
auth = Blueprint("auth", __name__, url_prefix="/auth")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        secret_key = current_app.config['SECRET_KEY']

        if not token:
            return jsonify({"error": "Token is missing"}), 401
        try:
            data = jwt.decode(token, secret_key, algorithms=["HS256"])
            kwargs["current_user"] = storage.get_by_email(User, data['email'])
            session.setdefault('logged_in', True)
        except:
            return jsonify({"error": "Token is invalid"}), 401
        return f(*args, **kwargs)
    return decorated


from app.views.user import *
from app.views.userProfile import *
from app.views.skill import *
from app.views.message import *
from app.views.jobs import *

from app.models.skills import Skills
from app.models.education import Education
from app.models.userEducation import UserEducation
from app.models.user_skills import UserSkills
from app.models.experience import Experience
from app.models.userExperience import UserExperience
from app.models.user import User
from app.models.notification import Notification
from app.models.message import Messages
from app.models import storage
from app.models.JobPostings import Job
# import storage engine and class
