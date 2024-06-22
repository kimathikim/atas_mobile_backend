from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from app.models.base_model import Base, BaseClass


class Notification(BaseClass, Base):
    __tablename__ = 'notifications'

    UserID = Column(String(60), ForeignKey('users.id'))
    NotificationType = Column(String(60))
    Message = Column(String(255))
    IsRead = Column(Boolean, default=False)

    user = relationship('User', backref='notifications')
