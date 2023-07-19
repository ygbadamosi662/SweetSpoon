#!/usr/bin/python3

"""
    Initialize the storage module
"""
from models.engine import db_storage


storage = db_storage.DBStorage()
storage.reload()
    
__all__ = []