from fastapi import FastAPI, HTTPException, Response,status, Depends, APIRouter
from typing import  List
from app import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import  get_db
from .. import oauth2

router = APIRouter(
    prefix="/sqlalchemy/posts", #all routes in this file will have /sqlalchemy/posts as prefix
    tags=["SQLAlchemy Posts"] #grouping the routes under this tag in the docs
)



# # path operation
# @router.get("/")  #get request, there are other methods like post, put, delete
# async def root(): #async is used for asynchronous programming, but not mandatory
#      return {"message": "Welcome to my FastAPI application!!!!!!"}


#
# Best CRUD practices for URLs
# Create - POST - /posts
# Read - GET - /posts or /posts/{id}
# Update - PUT - /posts/{id} or PATCH - /posts/{id}
# Delete - DELETE - /posts/{id}

# my_posts = [{"title": "First Post", "content": "Content of the first post", "id": 1},
#             {"title": "favorite food", "content": "I like pizza", "id": 2}]

     
#Create a post method using SQLAlchemy
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_post_sqlalchemy(post: schemas.PostCreate, 
                           db: Session = Depends(get_db), 
                           current_user: models.User_alchemy= Depends(oauth2.get_current_user)): 
    print(current_user.email)
    print(post.model_dump())
    db_post = models.Post_alchemy(owner_id=current_user.id,**post.model_dump()) #unpacking the post dictionary to match the model fields
    db.add(db_post)
    db.commit()
    db.refresh(db_post)  #to get the updated instance with the generated ID
    return db_post

# @router.post("/sqlalchemy/posts",status_code=status.HTTP_201_CREATED)
# def create_post_sqlalchemy(post: schemas.PostCreate, db: Session = Depends(get_db)):
#     db_post = models.Post_alchemy(title=post.title, content=post.content, published=post.published)
#     db.add(db_post)
#     db.commit()
#     db.refresh(db_post)  #to get the updated instance with the generated ID
#     return db_post



#now let's create a path operation to get a specific post by id

# def find_post(id:int):
#     for post in my_posts:
#         if post['id'] == id:
#             return post
        

 #Path order matters, specific paths should be defined before dynamic paths, eg
# @router.get("/latest")
# def get_latest_post():
#     latest_post = my_posts[-1]
#     return {"latest_post": latest_post}
       
#get all posts method with SQLAlchemy
@router.get("/",response_model=List[schemas.Post])
def test_sqlalchemy(db: Session = Depends(get_db),
                    current_user: models.User_alchemy = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post_alchemy).all()
    return posts

#get all posts of the current logged in user with SQLAlchemy
@router.get("/my_posts",response_model=List[schemas.Post])
def get_my_posts_sqlalchemy(db: Session = Depends(get_db),
                           current_user: models.User_alchemy = Depends(oauth2.get_current_user)):   
    posts = db.query(models.Post_alchemy).filter(models.Post_alchemy.owner_id == current_user.id).all()
    return posts



# get one post by id using SQLAlchemy
@router.get("/{id}",response_model=schemas.Post)
def get_post_sqlalchemy(id:int, 
                        db: Session = Depends(get_db)):
    post = db.query(models.Post_alchemy).filter(models.Post_alchemy.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
    return  post

#instead of hard coding status codes, we can also use HTTPException

#now let's create a path operation to delete a specific post by id

# def find_post_index(id:int):
#     for index, post in enumerate(my_posts):
#         if post['id'] == id:
#             return index


#delete a post by id using SQLAlchemy
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post_sqlalchemy(id:int, 
                           db: Session = Depends(get_db),
                           current_user:models.User_alchemy= Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post_alchemy).filter(models.Post_alchemy.id == id)
    post=post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
    if post.owner_id != current_user.id: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail="Not authorized to perform requested action")
    post_query.delete(synchronize_session=False)
    db.commit()
    #return Response(status_code=status.HTTP_204_NO_CONTENT) 


#update a post by id using SQLAlchemy
@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Post)
def update_post_sqlalchemy(id:int, 
                           updated_post: schemas.PostCreate, 
                           db: Session = Depends(get_db),
                           current_user: models.User_alchemy = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post_alchemy).filter(models.Post_alchemy.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id: {id} was not found")
    if post.owner_id != current_user.id: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail="Not authorized to perform requested action")   
    post_query.update(updated_post.model_dump(), synchronize_session=False) # type: ignore
    db.commit()
    return post_query.first()
