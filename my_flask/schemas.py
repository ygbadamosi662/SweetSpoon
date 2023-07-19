"""Defines schemas using marshmallow for our request dtos"""
from marshmallow import fields, Schema, ValidationError
import re


def validate_phone_number(phone_number):
    # checks if the phone number matches (8 or 7 or 9 or 2)(0 or 1)(then any number from 0-9 8 times), the leading 0 in nigerian phone numbers is ignored in this case, so it expects a nigerian number without the leading 0
    pattern = r'^[8792][01]\d{8}$'
    if not re.match(pattern, phone_number):
        raise ValidationError('Invalid phone number format')