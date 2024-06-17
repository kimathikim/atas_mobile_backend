from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseClass

class Notifications(Base):
    __tablename__ = 'notifications'
    UserID = Column(Integer, ForeignKey('users.id'))
    NotificationType = Column(String)
    Message = Column(String)
    IsRead = Column(Boolean)

    user = relationship("Users")
