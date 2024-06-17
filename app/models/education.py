from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from app.models.base_model import Base, BaseClass
from sqlalchemy.orm import relationship


class Education(BaseClass, Base):
    __tablename__ = 'education'
    InstitutionName = Column(String(255), nullable=False)
    Degree = Column(String(255), nullable=False)
    FieldOfStudy = Column(String(255), nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
