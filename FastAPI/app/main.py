from random import randrange
from time import time
from fastapi import FastAPI, HTTPException, Response,status, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2 #postgres database adapter
from psycopg2.extras import RealDictCursor #to get the column names along with the data

from . import models
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, get_db

models.Base.metadata.create_all(bind=engine) #create the database tables

app=FastAPI() #fastapi instance



# path operation
@app.get("/")  #get request, there are other methods like post, put, delete
async def root(): #async is used for asynchronous programming, but not mandatory
     return {"message": "Welcome to my FastAPI application!!!!!!"}

#@app.get("/posts")
#def get_posts():
#    return [{"data_1":  "This is the content of the first post."},
#            {"data_2":   "This is the content of the second post. but i made some changes here."}]


#@app.post("/createposts")
#def create_posts(post: dict = Body(...)):
 #    print(post)
  #   return {"new_post": f"Post created! title: {post['title']} content: {post['content']} "}

#title str, content str,  do not add anything else
# using pydantic models for data validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True  #default value
    #rating: Optional[int] = None  #optional field


# set up our connection to the database
while True:
    try:
        conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',
                            password='Toi&moi=1',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Database connection failed!")
        print("Error:", error)
        time.sleep(4) #wait for 4 seconds before retrying



@app.post("/createposts")
def create_posts(new_post:Post):
     print(new_post.title)
     return {"data": new_post.title} #returning the pydantic model instance directly

# Best CRUD practices for URLs
# Create - POST - /posts
# Read - GET - /posts or /posts/{id}
# Update - PUT - /posts/{id} or PATCH - /posts/{id}
# Delete - DELETE - /posts/{id}

my_posts = [{"title": "First Post", "content": "Content of the first post", "id": 1},
            {"title": "favorite food", "content": "I like pizza", "id": 2}]

# @app.post("/posts",status_code=status.HTTP_201_CREATED)
# def create_post(post: Post):
#      post_dict = post.model_dump() #converting pydantic model to dictionary
#      post_dict['id'] = randrange(0,1000000) #generating random id
#      my_posts.append(post_dict)
#      print(post.title)
#      print(post_dict)
#      return {"data": post_dict}
# @app.post("/posts",status_code=status.HTTP_201_CREATED)

# create a post method using regular SQL with psycopg2
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute("INSERT INTO social_media_posts (title, content,published) VALUES (%s, %s,%s) RETURNING *",
                    (post.title, post.content, post.published))
    new_post=cursor.fetchone() #fetch the newly created post
    conn.commit() #to save the changes to the database (CRUCIAL STEP!!!)
    #print(new_post)
    return {"data": new_post}
     
#Create a post method using SQLAlchemy
@app.post("/sqlalchemy/posts",status_code=status.HTTP_201_CREATED)
def create_post_sqlalchemy(post: Post, db: Session = Depends(get_db)):
    print(post.model_dump())
    db_post = models.Post_alchemy(**post.model_dump()) #unpacking the post dictionary to match the model fields
    db.add(db_post)
    db.commit()
    db.refresh(db_post)  #to get the updated instance with the generated ID
    return db_post

# @app.post("/sqlalchemy/posts",status_code=status.HTTP_201_CREATED)
# def create_post_sqlalchemy(post: Post, db: Session = Depends(get_db)):
#     db_post = models.Post_alchemy(title=post.title, content=post.content, published=post.published)
#     db.add(db_post)
#     db.commit()
#     db.refresh(db_post)  #to get the updated instance with the generated ID
#     return {"data": db_post}



#now let's create a path operation to get a specific post by id

def find_post(id:int):
    for post in my_posts:
        if post['id'] == id:
            return post
        

 #Path order matters, specific paths should be defined before dynamic paths, eg
@app.get("/posts/latest")
def get_latest_post():
    latest_post = my_posts[-1]
    return {"latest_post": latest_post}
       
#get a post method with SQLAlchemy
@app.get("/sqlachemy/posts")
def test_sqlalchemy(db: Session = Depends(get_db)):
    posts = db.query(models.Post_alchemy).all()
    return {"data": posts}


#get all posts using regular SQL with psycopg2
@app.get("/posts")
def get_posts():
    cursor.execute("SELECT * FROM social_media_posts") #this line alone does not fetch data
    posts=cursor.fetchall() #fetch all the results from the executed query
    print(posts)
    return {"data": posts}

# @app.get("/posts/{id}")
# def get_post(id: int,response:Response):
#      post=find_post(id)
#      if not post:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                              detail=f"post with id: {id} was not found")
#          #response.status_code=status.HTTP_404_NOT_FOUND
#          #return {"message": f"post with id: {id} was not found"}
#      return {"post_details": post} 

# get one post using regular SQL with psycopg2
@app.get("/posts/{id}")
def get_post(id:int):
    cursor.execute("SELECT * FROM social_media_posts WHERE id = %s",(str(id),)) #don't forget the comma to make it a tuple
    post=cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
        #response.status_code=status.HTTP_404_NOT_FOUND
        #return {"message": f"post with id: {id} was not found"}
    return {"post_details": post} 

# get one post by id using SQLAlchemy
@app.get("/sqlalchemy/posts/{id}")
def get_post_sqlalchemy(id:int, db: Session = Depends(get_db)):
    post = db.query(models.Post_alchemy).filter(models.Post_alchemy.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
    return {"post_details": post}

#instead of hard coding status codes, we can also use HTTPException

#now let's create a path operation to delete a specific post by id

def find_post_index(id:int):
    for index, post in enumerate(my_posts):
        if post['id'] == id:
            return index

    # @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
    # def delete_post(id: int):
    #      post=find_post(id) #or index=find_post_index(id)
    #      if not post:# or if index is None:
    #          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                              detail=f"post with id: {id} was not found")
    #      my_posts.remove(post) #or my_posts.pop(index)
    #      return Response(status_code=status.HTTP_204_NO_CONTENT)


# delete a post using regular SQL with psycopg2
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("DELETE FROM social_media_posts WHERE id = %s RETURNING *",(str(id),))
    deleted_post=cursor.fetchone()
    conn.commit()
    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#delete a post by id using SQLAlchemy
@app.delete("/sqlalchemy/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post_sqlalchemy(id:int, db: Session = Depends(get_db)):
    post = db.query(models.Post_alchemy).filter(models.Post_alchemy.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT) 

#now let's create a path operation to update a specific post by id

# @app.put("/posts/{id}",status_code=status.HTTP_200_OK)
# def update_post(id: int, updated_post: Post):
#      index=find_post_index(id)
#      if index is None:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                              detail=f"post with id: {id} was not found")
#      updated_post_dict = updated_post.model_dump()
#      updated_post_dict['id'] = id
#      my_posts[index] = updated_post_dict #updating the post in the list with the new data
#      return {"data": updated_post_dict}

# update a post using regular SQL with psycopg2

@app.put("/posts/{id}",status_code=status.HTTP_200_OK)
def update_post(id: int, updated_post: Post):
    cursor.execute("UPDATE social_media_posts SET title = %s, content = %s, published=%s WHERE id = %s RETURNING *",
                    (updated_post.title, updated_post.content, updated_post.published, str(id)))
    row=cursor.fetchone()
    conn.commit()
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
    return {"data": row}

#update a post by id using SQLAlchemy
@app.put("/sqlalchemy/posts/{id}",status_code=status.HTTP_200_OK)
def update_post_sqlalchemy(id:int, updated_post: Post, db: Session = Depends(get_db)):
    post_query = db.query(models.Post_alchemy).filter(models.Post_alchemy.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
    post_query.update(updated_post.model_dump(), synchronize_session=False) # type: ignore
    db.commit()
    return {"data": post_query.first()}