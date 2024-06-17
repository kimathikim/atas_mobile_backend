from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.models.base_model import Base, BaseClass
# import relationship
from app.models.user import User
from sqlalchemy.orm import relationship


class Job(BaseClass, Base):
    __tablename__ = 'jobs'
    EmployerID = Column(String(60), ForeignKey('users.id'), nullable=False)
    JobTitle = Column(String(255), nullable=False)
    JobDescription = Column(String(1000), nullable=True)
    JobType = Column(String(50), nullable=True)
    SalaryRange = Column(String(100), nullable=True)
    Location = Column(String(255), nullable=True)
    Requirements = Column(String(500), nullable=True)
    employer = relationship('User', back_populates='jobs')
    User.jobs = relationship('Job',  back_populates='employer')
