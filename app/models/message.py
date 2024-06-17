from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseClass, Base


class Messages(BaseClass, Base):
    __tablename__ = 'messages'
    SenderID = Column(String(60), ForeignKey('users.id'))
    ReceiverID = Column(String(60), ForeignKey('users.id'))
    Content = Column(String(110))
    IsRead = Column(Boolean)

    sender = relationship("User", foreign_keys=[SenderID])
    receiver = relationship("User", foreign_keys=[ReceiverID])
