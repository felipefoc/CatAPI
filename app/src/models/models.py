from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from src.config.database import Base

class Cat(Base):
    __tablename__ = 'cats'

    id = Column(Integer, primary_key=True, index=True)
    breed = Column(String)
    location_of_origin = Column(String)
    coat_length = Column(String)
    body_type = Column(String)
    pattern = Column(String)