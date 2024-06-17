from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseClass, Base


class UserSkills(BaseClass, Base):
    """This class represents the skills of a user."""
    __tablename__ = 'user_skills'

    UserID = Column(String(60), ForeignKey('users.id'))
    SkillID = Column(String(60), ForeignKey('skills.id'))
    ProficiencyLevel = Column(String(60))

    # Relationships
    user = relationship("User", backref="user_skills")
    skill = relationship("Skills", backref="user_skills")
