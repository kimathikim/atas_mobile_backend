from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseClass, Base


class Notifications(BaseClass, Base):
    __tablename__ = 'notifications'

    UserID = Column(Integer, ForeignKey('users.id'))
    NotificationType = Column(String)
    Message = Column(String)
    IsRead = Column(Boolean)


    user = relationship("Users", foreign_keys=[UserID])
