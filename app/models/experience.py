from sqlalchemy import Column, Integer, String, DateTime
from app.models.base_model import Base, BaseClass


class Experience(BaseClass, Base):
    __tablename__ = 'experience'

    JobTitle = Column(String(60))
    CompanyName = Column(String(60))
    StartDate = Column(DateTime)
    EndDate = Column(DateTime)
    Description = Column(String(304))
