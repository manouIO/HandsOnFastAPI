from .database import Base
from sqlalchemy import  Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
# from sqlalchemy.dialects.postgresql import TIMESTAMP #specific to PostgreSQL
from sqlalchemy.sql.expression import null, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[int] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Post(Base):
    __tablename__ = "posts"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title : Mapped[str] = mapped_column(String, nullable=False)
    content : Mapped[str] = mapped_column(String, nullable=False)
    published : Mapped[bool]= mapped_column(Boolean, server_default='TRUE', nullable=False)
    created_at : Mapped[datetime]= mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) 
    owner_id : Mapped[int]=mapped_column( ForeignKey("users.id",ondelete="CASCADE"), nullable=False)

    owner=relationship("User")  #establishing relationship between User and Post models
    #to access the user who created the post

#Create a Vote model to represent the votes table
class Vote(Base):
    __tablename__ = "votes"

    user_id : Mapped[int]= mapped_column(Integer, ForeignKey("users.id",ondelete="CASCADE"), primary_key=True)
    post_id : Mapped[int]= mapped_column(Integer, ForeignKey("posts.id",ondelete="CASCADE"), primary_key=True)