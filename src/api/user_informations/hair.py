from pydantic import BaseModel

class Hair(BaseModel):
    color: str
    type: str

