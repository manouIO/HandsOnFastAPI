import time 
from fastapi import FastAPI, HTTPException, Response,status
#from fastapi.params import Body
from typing import List
import psycopg2 #postgres database adapter
from psycopg2.extras import RealDictCursor #to get the column names along with the data
from app import schemas
from .database import engine, SessionLocal, get_db


app=FastAPI() #fastapi instance

#set up our connection to the database
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



# @app.post("/createposts")
# def create_posts(post: dict = Body(...)):
#     print(post)
#     return {"new_post": f"Post created! title: {post['title']} content: {post['content']} "}



#now let's create a path operation to update a specific post by id

# @app.put("/posts/{id}",status_code=status.HTTP_200_OK)
# def update_post(id: int, updated_post: schemas.PostCreate):
#      index=find_post_index(id)
#      if index is None:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                              detail=f"post with id: {id} was not found")
#      updated_post_dict = updated_post.model_dump()
#      updated_post_dict['id'] = id
#      my_posts[index] = updated_post_dict #updating the post in the list with the new data
#      return  updated_post_dict

#update a post using regular SQL with psycopg2

@app.put("/posts/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate):
    cursor.execute("UPDATE social_media_posts SET title = %s, content = %s, published=%s WHERE id = %s RETURNING *",
                    (updated_post.title, updated_post.content, updated_post.published, str(id)))
    row=cursor.fetchone()
    conn.commit()
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
    return row


# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     post=find_post(id) #or index=find_post_index(id)
#     if not post:# or if index is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
#     my_posts.remove(post) #or my_posts.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


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


#get all posts using regular SQL with psycopg2
@app.get("/posts",response_model=List[schemas.Post])
def get_posts():
    cursor.execute("SELECT * FROM social_media_posts") #this line alone does not fetch data
    posts=cursor.fetchall() #fetch all the results from the executed query
    print(posts)
    return posts

# @app.get("/posts/{id}")
# def get_post(id: int,response:Response):
#      post=find_post(id)
#      if not post:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                              detail=f"post with id: {id} was not found")
#          #response.status_code=status.HTTP_404_NOT_FOUND
#          #return {"message": f"post with id: {id} was not found"}
#      return {"post_details": post} 

#get one post using regular SQL with psycopg2
@app.get("/posts/{id}")
def get_post(id:int):
    cursor.execute("SELECT * FROM social_media_posts WHERE id = %s",(str(id),)) #don't forget the comma to make it a tuple
    post=cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
        #response.status_code=status.HTTP_404_NOT_FOUND
        #return {"message": f"post with id: {id} was not found"}
    return  post


# @app.post("/posts",status_code=status.HTTP_201_CREATED)
# def create_post(post: schemas.PostCreate):
#      post_dict = post.model_dump() #converting pydantic model to dictionary
#      post_dict['id'] = randrange(0,1000000) #generating random id
#      my_posts.append(post_dict)
#      print(post.title)
#      print(post_dict)
#      return {post_dict}

# create a post method using regular SQL with psycopg2
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate):
    cursor.execute("INSERT INTO social_media_posts (title, content,published) VALUES (%s, %s,%s) RETURNING *",
                    (post.title, post.content, post.published))
    new_post=cursor.fetchone() #fetch the newly created post
    conn.commit() #to save the changes to the database (CRUCIAL STEP!!!)
    #print(new_post)
    return new_post