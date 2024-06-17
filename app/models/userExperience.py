from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseClass


class UserExperience(BaseClass, Base):
    __tablename__ = 'user_experience'

    UserExperienceID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('users.id'))
    ExperienceID = Column(Integer, ForeignKey('experience.ExperienceID'))

    user = relationship("Users", foreign_keys=[UserID])
    experience = relationship("Experience", foreign_keys=[ExperienceID])
