from app.models.base_model import BaseClass, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.user import User


class Skills(BaseClass, Base):
    """This class represents the skills of a user."""
    __tablename__ = 'skills'
    SkillName = Column(String(255), nullable=False)
