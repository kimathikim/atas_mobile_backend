from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1/")
auth = Blueprint("auth", __name__, url_prefix="/auth")

from app.views.user import *
from app.views.userProfile import *
from app.views.skill import *
from app.views.message import *

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

# import storage engine and class
