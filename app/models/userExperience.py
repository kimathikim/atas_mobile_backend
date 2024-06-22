from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseClass


class UserExperience(BaseClass, Base):
    __tablename__ = 'user_experience'
    UserID = Column(String(60), ForeignKey('users.id'))
    ExperienceID = Column(String(60), ForeignKey('experience.id'))

    user = relationship("User", foreign_keys=[UserID])
    experience = relationship("Experience", foreign_keys=[ExperienceID])
