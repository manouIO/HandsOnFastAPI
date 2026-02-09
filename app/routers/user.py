from fastapi import FastAPI, HTTPException, Response,status, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="sqlalchemy/users",
    tags=['Users']
)



# Create a user using SQLAlchemy
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.User)
def create_user_sqlalchemy(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print("==========================")
    hashed_password = utils.hash_password(user.password) #hash the password before storing
    user.password = hashed_password 
    db_user = models.User(**user.model_dump()) #unpacking the user dictionary to match the model fields
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  #to get the updated instance with the generated ID
    return db_user

# Get a user by id using SQLAlchemy
@router.get("/{id}",response_model=schemas.User)
def get_user_sqlalchemy(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"user with id: {id} was not found")
    return  user