from fastapi import FastAPI
from app import models
from .database import engine
from .routers import post, user, auth,vote

models.Base.metadata.create_all(bind=engine) #create the database tables

app=FastAPI() #fastapi instance


  
app.include_router(post.router) #include the post router
app.include_router(user.router) 
app.include_router(auth.router) #include the auth router
app.include_router(vote.router) #include the vote router