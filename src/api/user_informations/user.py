from pydantic import BaseModel, EmailStr, HttpUrl
from .address import Address
from .crypto import Crypto
from .hair import Hair
from .company import Company
from .bank import Bank

class User(BaseModel):
    id: int
    firstName: str
    lastName: str
    maidenName: str
    age: int
    gender: str
    email: EmailStr
    phone: str
    username: str
    password: str
    birthDate: str
    image: HttpUrl
    bloodGroup: str
    height: float
    weight: float
    eyeColor: str
    hair: Hair
    ip: str
    address: Address
    macAddress: str
    university: str
    bank: Bank
    company: Company
    ein: str
    ssn: str
    userAgent: str
    crypto: Crypto
    role: str