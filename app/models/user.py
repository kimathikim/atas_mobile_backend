#!/usr/bin/env python3

'''This module defines the User class'''
from app.models.base_model import BaseClass, Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship


class User(BaseClass, Base):
    '''This class defines the User class'''
    __tablename__ = 'users'
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    user_type = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True)
    jobs = relationship('Job', back_populates='Employer')
