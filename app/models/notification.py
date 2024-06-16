from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseClass


class Users(Bapp/models/engine/__pycache__/dbStorage.cpython-310.pycaseClass, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)


class Notifications(Base):
    __tablename__ = 'notifications'
    UserID = Column(Integer, ForeignKey('users.id'))
    NotificationType = Column(String)
    Message = Column(String)
    IsRead = Column(Boolean)

    user = relationship("Users")
