"""Defines the Utility class"""
from models import storage
from sqlalchemy import exists
from typing import Union, List
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity
from global_vars import USER
from models.user import User
from Repos.userRepo import user_repo


class Utility:
    """
    Defines Utility class, just for utility functions
    """
    _session = None

    def __init__(self):
        self._session = storage.get_session()

    def getInstanceFromJwt(self) -> User:
        payload = get_jwt_identity()
        try:
            user = user_repo.findByEmail(payload['email'])
            return user
        except SQLAlchemyError:
            raise SQLAlchemyError('fetching user by email from get_jwt_identity failed', 'from util')

    def persistModel(self, model):
        storage.new(model)
        storage.save()

    def closeSession(self):
        storage.close()

    def validate_table_integrity_byEmail(self, email: str, model: str) -> bool:
        # this method checks if a certain mapped instance already exists in its table by its email
        if model == USER:
            exists_query = self._session.query(exists().where(User.email == email))

        return self._session.scalar(exists_query)
    
    def validate_table_integrity_byPhone(self, phone: str, model: str) -> bool:
        # this method checks if a certain mapped instance already exists in its table by phone
        if model == USER:
            exists_query = self._session.query(exists().where(User.phone == phone))

        return self._session.scalar(exists_query)


util = Utility()
