from pydantic import BaseModel

class Crypto(BaseModel):
    coin: str
    wallet: str
    network: str