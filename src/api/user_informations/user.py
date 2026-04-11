from pydantic import BaseModel, EmailStr, HttpUrl
from .address import Address
from .crypto import Crypto
from .hair import Hair
from .company import Company
from .bank import Bank

class User():
    EXPECTED_KEYS = {
        "id": int,
        "firstName": str,
        "lastName": str,
        "maidenName": str,
        "age": int,
        "gender": str,
        "email": EmailStr,
        "phone": str,
        "username": str,
        "password": str,
        "birthDate": str,
        "image": HttpUrl,
        "bloodGroup": str,
        "height": float,
        "weight": float,
        "eyeColor": str,
        "hair": dict,
        "ip": str,
        "address": dict,
        "macAddress": str,
        "university": str,
        "bank": dict,
        "company": dict,
        "ein": str,
        "ssn": str,
        "userAgent": str,
        "crypto": dict,
        "role": str
    }

    @staticmethod
    def from_dict(data: dict):
        return User(**data)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def assert_expected_keys_exist_and_types_are_valid(self):
        for field, expected_type in self.EXPECTED_KEYS.items():
            if expected_type == EmailStr or expected_type == HttpUrl:
                expected_type = str
            assert isinstance(getattr(self, field), expected_type), \
            f"Expected {field} to have type {expected_type}, got {type(getattr(self, field))} instead"

    