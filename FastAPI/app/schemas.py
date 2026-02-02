from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

#title str, content str,  do not add anything else
# using pydantic models for data validation
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True  #default value
    #owner_id: int #we won't include owner_id here as it will be set from the token

class PostCreate(PostBase):
    pass

#Schema for User response model
class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    # class Config: #we want to work with ORM objects
    #     orm_mode = True
    model_config = {"from_attributes": True}

#Let's create a schema for the post response model
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: User #forward reference to User schema
    
    class Config:
        orm_mode = True  #to work with ORM objects like SQLAlchemy


#Schemas for User
class UserCreate(BaseModel):
    email: EmailStr
    password: str 



#Schema for User login
class UserLogin(UserCreate):
    pass

#Schema for Token
class Token(BaseModel):
    access_token: str
    token_type: str

#Schema for Token Data
class TokenData(BaseModel):
    id: Optional[str] = None # or Optional[int] depending on your user id type