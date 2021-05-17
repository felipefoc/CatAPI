from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schema import schemas
from src.models import Cat


class ControllerCat():

    def __init__(self, session: Session):
        self.session = session

    def create(self, cat: schemas.Cat):
        data = Cat(breed=Cat.breed,
                location_of_origin=Cat.location_of_origin,
                coat_length=Cat.coat_length,
                body_type=Cat.body_type,
                pattern=Cat.pattern)
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        return data
