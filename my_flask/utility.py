"""Defines the Utility class"""
from models import storage
from sqlalchemy import exists
from typing import Union, List
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity


class Utility:
    """
    Defines Utility class, just for utility functions
    """
    session = None

    def __init__(self):
        self.session = storage.get_session()