#!/usr/bin/env python3
"""This claass defines the database storage engine for the
immunization tracking system"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.models.base_model import Base
from app.models.user import User
from app.models.company import Company
from app.models.JobPostings import Job
from app.models.skills import Skills
from app.models.user_skills import UserSkills
from app.models.location import Location
from app.models.experience import Experience
from app.models.userExperience import UserExperience
from app.models.education import Education
from app.models.message import Messages
from app.models.userEducation import UserEducation
from app.models.notification import Notification

classes = {
    User: User,
    Company.__name__: Company,
    Job.__name__: Job,
    Location.__name__: Location,
    Education.__name__: Education,
    Messages.__name__: Messages,
    UserEducation.__name__: UserEducation,
    Skills.__name__: Skills,
    UserSkills.__name__: UserSkills,
    Experience.__name__: Experience,
    UserExperience.__name__: UserExperience,
    Notification.__name__: Notification,
}


class DBstorage:
    """Initialize with the MySQL database"""


class DBStorage:
    def __init__(self):
        """Initialize the data storage class"""
        AM_USER = os.getenv("AM_USER")
        AM_PWD = os.getenv("AM_PWD")
        AM_HOST = os.getenv("AM_HOST")
        AM_DB = os.getenv("AM_DB")

        self.__engine = create_engine(
            "mysql+pymysql://{}:{}@{}/{}".format(AM_USER,
                                                 AM_PWD, AM_HOST, AM_DB),
            pool_pre_ping=True,
        )

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def new(self, obj):
        """add the object to the current database sesson"""
        self.__session.add(obj)

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and
        the current database session"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """closes the session"""
        self.__session.close()

    def get(self, cls, id):
        """get an object from the database"""
        if cls is not None and id is not None:
            obj = self.__session.query(cls).get(id)
            return obj
        return None

    # get object by email
    def get_by_email(self, cls, email):
        """get an object from the database"""
        if cls is not None and email is not None:
            obj = self.__session.query(cls).filter_by(email=email).first()
            return obj
        return None
