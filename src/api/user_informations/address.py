from pydantic import BaseModel
from .coordinates import Coordinates


class Address(BaseModel):
    address: str
    city: str
    state: str
    stateCode: str
    postalCode: str
    coordinates: Coordinates
    country: str
