#!/usr/bin/python3
"""Defines the Subject class."""
from models.base_model import Base, BaseModel
import uuid
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column



class Subject(BaseModel, Base):
    """Represents a Subject class, a super class extends Base from sqlalchemy
    Attributes:
        __tablename__ (str): The name of the MySQL table to store
        subjects.
    """
    __tablename__ = "subjects"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=str(uuid.uuid4()), unique=True)
    name: Mapped[str] = mapped_column(String(128))

    # subjects = relationship("Notification", back_populates="subject")

    __mapper_args__ = {
        "polymorphic_identity": "subject",
        "polymorphic_on": "name",
    }

    def __init__(self, name):
        self.name = name
