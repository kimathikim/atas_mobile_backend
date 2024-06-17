from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.models.base_model import Base, BaseClass

class Job(BaseClass,Base):
    __tablename__ = 'jobs'
    EmployerID = Column(Integer, ForeignKey('users.UserID'), nullable=False)
    JobTitle = Column(String(255), nullable=False)
    JobDescription = Column(Text, nullable=True)
    JobType = Column(String(50), nullable=True)
    SalaryRange = Column(String(100), nullable=True)
    Location = Column(String(255), nullable=True)
    Requirements = Column(Text, nullable=True)
    
    employer = relationship('User', back_populates='jobs')

    User.jobs = relationship('Job', order_by=Job.JobID, back_populates='employer')

