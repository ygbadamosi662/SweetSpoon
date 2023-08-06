#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel, Base
import uuid
from sqlalchemy import Date
from sqlalchemy import String
from global_vars import globalBcrypt
from sqlalchemy.orm import relationship, Mapped, mapped_column
from Enums.gender import Gender
from Enums.role import Role


class User(BaseModel, Base):
    """
    Represents a user for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table users.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        id: (sqlalchemy Integer, Primary_key): user's id
        name: (sqlalchemy String): The user's name.
        email: (sqlalchemy String): The user's email.
        phone: (sqlalchemy String): The user's phone.
        gender: (sqlalchemy Enum): The user's gender
        role: (sqlalchemy Enum): The user's role
    """
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=str(uuid.uuid4()), unique=True)
    first_name: Mapped[str] = mapped_column(String(128))
    last_name: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(128), nullable=False) #this will be set unique=True eventually
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    gender: Mapped[Gender]
    dob = mapped_column(Date)
    role: Mapped[Role]

    orders = relationship("Order", back_populates="user")
    accounts = relationship("Account", back_populates="user")

    
    __mapper_args__ = {
        "polymorphic_identity": "user",
    }

    def __init__(self, *args, **kwargs):
        """Initialize guardian"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with bcrypt encryption"""
        if name == "password":
            value = globalBcrypt.hashpw(value.encode('utf-8'), globalBcrypt.gensalt())
        super().__setattr__(name, value)
