from fastapi import FastAPI
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.schema.schemas import Cat
from src.config.database import get_db
from src.controller.cat import ControllerCat

app = FastAPI()


@app.post('/',status_code=status.HTTP_201_CREATED,
              response_model=Cat)
def signup(cat: Cat, session: Session = Depends(get_db)):
   return ControllerCat(session).create(cat)

@app.get("/")
async def root():
    return {"message": "Hello World"}