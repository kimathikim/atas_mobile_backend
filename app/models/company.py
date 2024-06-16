#!/usr/bin/env python3
'''This module defines the Company class'''
from app.models.base_model import BaseClass, Base
from sqlalchemy import Column, Integer, String, Text


class Company(BaseClass, Base):
    __tablename__ = 'company'

    CompanyName = Column(String(128), nullable=False)
    CompanyDescription = Column(Text, nullable=True)
    WebsiteURL = Column(String(128), nullable=True)
    Location = Column(String(128), nullable=True)
