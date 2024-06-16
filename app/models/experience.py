from sqlalchemy import Column, Integer, String, DateTime
from app.models.base_model import Base, BaseClass


class Experience(BaseClass, Base):
    __tablename__ = 'experience'

    ExperienceID = Column(Integer, primary_key=True)
    JobTitle = Column(String)
    CompanyName = Column(String)
    StartDate = Column(DateTime)
    EndDate = Column(DateTime)
    Description = Column(String)
