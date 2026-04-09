from pydantic import BaseModel

class Bank(BaseModel):
    cardExpire: str
    cardNumber: str
    cardType: str
    currency: str
    iban: str

