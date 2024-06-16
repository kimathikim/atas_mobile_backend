from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1/")
auth = Blueprint("auth", __name__, url_prefix="/auth")

from app.views.user import *
from app.models.user import User
from app.models import storage

# import storage engine and class
