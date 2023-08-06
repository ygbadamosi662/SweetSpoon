"""Defines Status Enum"""
from Enums import Enum


class Status(Enum):
    """ 
    represents Gender enum
    extends Enum from python enum

    Attributes:\n
    PENDING = 'PENDING            '\n
    COMPLETED = 'COMPLETED'\n
    FAILED = 'FAILED'\n
    """
    PENDING = 'PENDING            ' #this is not a mistake
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
