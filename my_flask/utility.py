"""Defines the Utility class"""
from models import storage
from sqlalchemy import exists
from typing import Union, List
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity
from global_vars import USER
from models.user import User


class Utility:
    """
    Defines Utility class, just for utility functions
    """
    session = None

    def __init__(self):
        self.session = storage.get_session()

    def persistModel(self, model):
        storage.new(model)
        storage.save()

    def closeSession(self):
        storage.close()

    def validate_table_integrity_byEmail(self, email: str, model: str) -> bool:
        # this method checks if a certain mapped instance already exists in its table, it only checks for schools, students and guardians table by their respective email for now
        if model == USER:
            exists_query = self.session.query(exists().where(User.email == email))


        return self.session.scalar(exists_query)
    
    def validate_table_integrity_byPhone(self, phone: str, model: str) -> bool:
        # this method checks if a certain mapped instance already exists in its table, it only checks for school and guardians by their phone number table for now
        if model == USER:
            exists_query = self.session.query(exists().where(User.phone == phone))

        return self.session.scalar(exists_query)


util = Utility()
