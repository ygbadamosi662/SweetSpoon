#!/usr/bin/python3
"""Defines the Food class."""
from models.subject import Subject
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from Enums.food_type import FoodType


class Food(Subject):
    """
    Represents a food for a MySQL database.
    Inherits from Subject and links to the MySQL table foods.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        id: (sqlalchemy Integer, Primary_key): food's id
        name: (sqlalchemy String): The food's name.
        price: (sqlalchemy String): The food's price.
        qty: (sqlalchemy Integer): The food's quantity.
        type: (sqlalchemy Enum): The food's type
    """
    __tablename__ = "foods"

    id: Mapped[str] = mapped_column(ForeignKey("subjects.id"), primary_key=True, name="food_id")
    food_name: Mapped[str] = mapped_column(String(128))
    description: Mapped[str] = mapped_column(String(1000))
    price: Mapped[str] = mapped_column(String(128))
    qty: Mapped[int] = mapped_column(Integer)
    type: Mapped[FoodType]

    orders = relationship("Order", foreign_keys="Order.order_id", back_populates="food")

    __mapper_args__ = {
        "polymorphic_identity": "food",
    }

    def __init__(self, *args, **kwargs):
        """Initialize food"""
        super().__init__(*args, **kwargs)
