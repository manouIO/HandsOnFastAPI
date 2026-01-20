import time 
from fastapi import FastAPI, HTTPException, Response,status, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
import psycopg2 #postgres database adapter
#from psycopg2.extras import RealDictCursor #to get the column names along with the data
from app import models, schemas, utils
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, get_db
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine) #create the database tables

app=FastAPI() #fastapi instance


  
app.include_router(post.router) #include the post router
app.include_router(user.router) 
app.include_router(auth.router) #include the auth router