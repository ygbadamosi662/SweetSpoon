#!/usr/bin/python3
"""Defines the Order class."""
from models.subject import Subject
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from Enums.derica import Derica
from Enums.tracking import Tracking


class Order(Subject):
    """
    Represents a order for a MySQL database.
    Inherits from Subject and links to the MySQL table orders.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        id: (sqlalchemy Integer, Primary_key): food's id
        total: (sqlalchemy Integer): The food's name.
        price: (sqlalchemy String): The food's price.
        qty: (sqlalchemy Integer): The food's quantity.
        type: (sqlalchemy Enum): The food's type
    """
    __tablename__ = "orders"

    id: Mapped[str] = mapped_column(ForeignKey("subjects.id"), primary_key=True, name="order_id")
    total: Mapped[int] = mapped_column(Integer)
    qty: Mapped[int] = mapped_column(Integer)
    derica: Mapped[Derica]
    how_far: Mapped[Tracking]

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    user = relationship("User", back_populates="orders")

    food_id: Mapped[str] = mapped_column(ForeignKey("foods.food_id"))
    food = relationship("Food", foreign_keys=food_id, backref="orders")

    transaction_id: Mapped[str]= mapped_column(ForeignKey('transactions.transaction_id'))
    transaction = relationship("Transaction", foreign_keys=transaction_id, back_populates="order")

    __mapper_args__ = {
        "polymorphic_identity": "order",
    }

    def __init__(self, *args, **kwargs):
        """Initialize order"""
        super().__init__(*args, **kwargs)
