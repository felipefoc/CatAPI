from pydantic import BaseModel
from typing import Optional


class Cat(BaseModel):
    id: Optional[int] = None
    breed: str
    location_of_origin: str
    coat_length: str
    body_type: str
    pattern: str

    class Config:
        orm_mode = True
