#!/usr/bin/python3
"""Defines the Account class."""
from models.subject import Subject
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column


class  Account(Subject):
    """
    Represents a account for a MySQL database.
    Inherits from Subject and links to the MySQL table foods.a
    Attributes:
        __tablename__ (str): The name of the MySQL table to store transactions.
        id: (sqlalchemy Integer, Primary_key): food's id
        name: (sqlalchemy String): The food's name.
        price: (sqlalchemy String): The food's price.
        qty: (sqlalchemy Integer): The food's quantity.
        type: (sqlalchemy Enum): The food's type
    """
    __tablename__ = "accounts"

    id: Mapped[str] = mapped_column(ForeignKey("subjects.id"), primary_key=True, name="account_id")
    account_name: Mapped[str] = mapped_column(String(255))
    bank_name: Mapped[str] = mapped_column(String(255))
    acc_number: Mapped[str] = mapped_column(String(128))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user = relationship("User", back_populates="accounts")

    transactions = relationship("Transaction", foreign_keys="Transaction.transaction_id", back_populates="account")

    __mapper_args__ = {
        "polymorphic_identity": "account",
    }

    def __init__(self, *args, **kwargs):
        """Initialize bank"""
        super().__init__(*args, **kwargs)
