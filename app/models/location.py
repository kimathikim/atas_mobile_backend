from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from app.models.base_model import Base, BaseClass


class User(BaseClass,Base):
    __tablename__ = 'users'
    UserName = Column(String(255), nullable=False)
    UserEmail = Column(String(255), nullable=False)

class Jobs(BaseClass,Base):
    __tablename__ = 'jobs'
    EmployerID = Column(Integer, ForeignKey('users.UserID'), nullable=False)
    JobTitle = Column(String(255), nullable=False)
    JobDescription = Column(String, nullable=True)
    JobType = Column(String(50), nullable=True)
    SalaryRange = Column(String(100), nullable=True)
    Location = Column(String(255), nullable=True)
    Requirements = Column(String, nullable=True)
    employer = relationship('User', back_populates='jobs')
    User.jobs = relationship('Jobs', order_by=Jobs.JobID, back_populates='employer')

class Location(BaseClass,Base):
    __tablename__ = 'locations'
    City = Column(String(255), nullable=False)
    State = Column(String(255), nullable=False)
    Country = Column(String(255), nullable=False)

class JobLocation(BaseClass,Base):
    __tablename__ = 'joblocations'
    JobID = Column(Integer, ForeignKey('jobs.JobID'), nullable=False)
    LocationID = Column(Integer, ForeignKey('locations.LocationID'), nullable=False)
    
    job = relationship('Job', back_populates='job_locations')
    location = relationship('Location', back_populates='job_locations')

    Job.job_locations = relationship('JobLocation', order_by=JobLocation.JobLocationID, back_populates='job')
    Location.job_locations = relationship('JobLocation', order_by=JobLocation.JobLocationID, back_populates='location')

