from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseClass, Base


class Messages(BaseClass, Base):
    __tablename__ = 'messages'

    MessageID = Column(Integer, primary_key=True)
    SenderID = Column(Integer, ForeignKey('users.id'))
    ReceiverID = Column(Integer, ForeignKey('users.id'))
    Content = Column(String)
    SentAt = Column(DateTime)
    IsRead = Column(Boolean)

    sender = relationship("Users", foreign_keys=[SenderID])
    receiver = relationship("Users", foreign_keys=[ReceiverID])
