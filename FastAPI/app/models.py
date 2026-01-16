from .database import Base
from sqlalchemy import  Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import null,text

class Post_alchemy(Base):
    __tablename__ = "social_media_posts_alchemy"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) 

class User_alchemy(Base):
    __tablename__ = "users_alchemy"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True) #ensure unique emails and prevent null values
    password = Column(String, nullable=False) # no need for unique passwords
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))