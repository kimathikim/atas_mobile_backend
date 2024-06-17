from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from app.models.base_model import Base, BaseClass


class Education(BaseClass,Base):
    __tablename__ = 'education'
    InstitutionName = Column(String(255), nullable=False)
    Degree = Column(String(255), nullable=False)
    FieldOfStudy = Column(String(255), nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)

class UserEducation(BaseClass,Base):
    __tablename__ = 'usereducation'
    UserID = Column(Integer, ForeignKey('users.UserID'), nullable=False)
    EducationID = Column(Integer, ForeignKey('education.EducationID'), nullable=False)
    
    user = relationship('User', back_populates='user_education')
    education = relationship('Education', back_populates='user_education')

    User.user_education = relationship('UserEducation', order_by=UserEducation.UserEducationID, back_populates='user')
    Education.user_education = relationship('UserEducation', order_by=UserEducation.UserEducationID, back_populates='education')

