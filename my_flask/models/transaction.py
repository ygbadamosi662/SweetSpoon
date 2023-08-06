#!/usr/bin/python3
"""Defines the Transaction class."""
from models.subject import Subject
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from Enums.status import Status
from Enums.tr_type import TrType


class Transaction(Subject):
    """
    Represents a transaction for a MySQL database.
    Inherits from Subject and links to the MySQL table foods.a
    Attributes:
        __tablename__ (str): The name of the MySQL table to store transactions.
        id: (sqlalchemy Integer, Primary_key): food's id
        name: (sqlalchemy String): The food's name.
        price: (sqlalchemy String): The food's price.
        qty: (sqlalchemy Integer): The food's quantity.
        type: (sqlalchemy Enum): The food's type
    """
    __tablename__ = "transactions"

    id: Mapped[str] = mapped_column(ForeignKey("subjects.id"), primary_key=True, name="transaction_id")
    amount: Mapped[int] = mapped_column(Integer)
    status: Mapped[Status]
    type: Mapped[TrType]

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.account_id"))
    account = relationship("Account", foreign_keys=account_id, backref="transactions")

    order = relationship("Order", foreign_keys="Order.transaction_id", uselist=False, back_populates="transaction")

    __mapper_args__ = {
        "polymorphic_identity": "transaction",
    }

    def __init__(self, *args, **kwargs):
        """Initialize transaction"""
        super().__init__(*args, **kwargs)
