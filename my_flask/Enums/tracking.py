"""Defines Tracking Enum"""
from Enums import Enum


class Tracking(Enum):
    """ 
    represents Tracking enum
    extends Enum from python enum

    Attributes:\n
    COOKING = 'COOKING            '\n
    READY = 'READY'\n
    ON_THE_WAY = 'OTW'\n
    DELIVERED = 'DELIVERED'\n
    """
    COOKING = 'COOKING            ' #this is not a mistake
    READY = 'READY'
    ON_THE_WAY = 'OTW'
    DELIVERED = 'DELIVERED'
