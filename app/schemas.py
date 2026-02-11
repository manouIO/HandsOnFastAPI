from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime
from typing import Optional, Literal

from pydantic_settings import SettingsConfigDict

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
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    # class Config: #we want to work with ORM objects
    #     orm_mode = True
    model_config = ConfigDict(from_attributes=True)

#Let's create a schema for the post response model
class Post(PostBase):
    id: int #the post id
    created_at: datetime
    #owner_id: int #we can include owner_id if needed but it is already contained in the owner field
    owner: UserOut #forward reference to User schema
    #votes: optional[int] = 0  #to include the number of votes for the post
    
    model_config = ConfigDict(from_attributes=True)  #to work with ORM objects like SQLAlchemy

#Let's create a schema for the post response model with votes
class PostOut(BaseModel):
    Post: Post #we must use a label in the db.query to avoid confusion because the original name is Post
    votes: int

    model_config = ConfigDict(from_attributes=True) #to work with ORM objects like SQLAlchemy

        
#Schemas for User
class UserCreate(BaseModel):
    email: EmailStr
    password: str 
    phone_number: Optional[str] = None



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


#Schema for Vote
class Vote(BaseModel):
    post_id: int
    dir: Literal[0,1]  #1 for upvote, 0 for removing vote    