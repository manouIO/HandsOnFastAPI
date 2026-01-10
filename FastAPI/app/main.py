from random import randrange
from fastapi import FastAPI, HTTPException, Response,status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


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
    rating: Optional[int] = None  #optional field

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

@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
     post_dict = post.model_dump() #converting pydantic model to dictionary
     post_dict['id'] = randrange(0,1000000) #generating random id
     my_posts.append(post_dict)
     print(post.title)
     print(post_dict)
     return {"data": post_dict}

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
       
@app.get("/posts/{id}")
def get_post(id: int,response:Response):
     post=find_post(id)
     if not post:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
         #response.status_code=status.HTTP_404_NOT_FOUND
         #return {"message": f"post with id: {id} was not found"}
     return {"post_details": post} 

#instead of hard coding status codes, we can also use HTTPException

#now let's create a path operation to delete a specific post by id

def find_post_index(id:int):
    for index, post in enumerate(my_posts):
        if post['id'] == id:
            return index

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
     post=find_post(id) #or index=find_post_index(id)
     if not post:# or if index is None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
     my_posts.remove(post) #or my_posts.pop(index)
     return Response(status_code=status.HTTP_204_NO_CONTENT)

#now let's create a path operation to update a specific post by id

@app.put("/posts/{id}",status_code=status.HTTP_200_OK)
def update_post(id: int, updated_post: Post):
     index=find_post_index(id)
     if index is None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
     updated_post_dict = updated_post.model_dump()
     updated_post_dict['id'] = id
     my_posts[index] = updated_post_dict #updating the post in the list with the new data
     return {"data": updated_post_dict}