from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from app.models.base_model import Base, BaseClass
from sqlalchemy.orm import relationship
from app.models.user import User
from app.models.JobPostings import Job


class Location(BaseClass,Base):
    __tablename__ = 'locations'
    City = Column(String(255), nullable=False)
    State = Column(String(255), nullable=False)
    Country = Column(String(255), nullable=False)

class JobLocation(BaseClass,Base):
    __tablename__ = 'joblocations'
    JobID = Column(String(60), ForeignKey('jobs.id'), nullable=False)
    LocationID = Column(String(60), ForeignKey('locations.id'), nullable=False)
    
    job = relationship('Job', back_populates='job_locations')
    location = relationship('Location', back_populates='job_locations')

    Job.job_locations = relationship('JobLocation',  back_populates='job')
    Location.job_locations = relationship('JobLocation', back_populates='location')

