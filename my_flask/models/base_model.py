#!/usr/bin/python3
"""Defines the BaseModel class."""
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime


time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


class BaseModel:
    """Defines the BaseModel class.
    Attributes:
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, time)
                    setattr(self, key, value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        model_name = type(self).__name__

        if hasattr(self, "id"):
            return "[{}] ({}) {}".format(model_name, self.id, d)
        else:
            return "[{}] {}".format(model_name, d)

    def save(self):
        """Update the time the changes were made."""
        self.updated_at = datetime.utcnow

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        if "created_at" in my_dict:
            my_dict["created_at"] = my_dict["created_at"].strftime(time)
        if "updated_at" in my_dict:
            my_dict["updated_at"] = my_dict["updated_at"].strftime(time)
        my_dict.pop("_sa_instance_state", None)
        if "password" in my_dict:
            del my_dict["password"]
        return my_dict