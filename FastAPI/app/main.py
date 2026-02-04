from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models
from .database import engine
from .routers import post, user, auth, vote

#models.Base.metadata.create_all(bind=engine) #create the database tables
# we don't need to create the tables here because we will use alembic to handle the database migrations
# ----- no to consider ----:
app=FastAPI() #fastapi instance
origins = ["*"]  # Allows all origins, ie any domain can access the API. but it is security 
                #best practice to limit this to only the domains you want to allow.

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


  
app.include_router(post.router) #include the post router
app.include_router(user.router) 
app.include_router(auth.router) #include the auth router
app.include_router(vote.router) #include the vote router

@app.get("/") #root endpoint
def root():
    return {"message":"Welcome to FastAPI!"}
