from pydantic import BaseModel
from .address import Address

class Company(BaseModel):
    department: str
    name: str
    title: str
    address: Address

