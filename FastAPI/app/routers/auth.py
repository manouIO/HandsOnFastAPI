from fastapi import FastAPI, HTTPException, Response,status, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from typing import  List
from ..import database, schemas, models, utils,oauth2
from sqlalchemy.orm import Session

router = APIRouter(
tags=["Authentications"] #grouping the routes under this tag in the docs
)       

@router.post("/login",response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(database.get_db)): 
    user = db.query(models.User_alchemy).filter(
        models.User_alchemy.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail="Invalid Credentials")
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail="Invalid Credentials")
    #return {"message": "Login successful!"}

    #create a token upon successful login
    access_token=oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
