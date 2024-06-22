from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from app.models.base_model import Base, BaseClass
from sqlalchemy.orm import relationship
from app.models.user import User
from app.models.education import Education


class UserEducation(BaseClass, Base):
    __tablename__ = 'usereducation'
    UserID = Column(String(60), ForeignKey('users.id'), nullable=False)
    EducationID = Column(String(60), ForeignKey(
        'education.id'), nullable=False)
