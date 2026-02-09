from fastapi import APIRouter, Depends, HTTPException, status,Response
from sqlalchemy.orm import Session
from .. import models, oauth2, schemas
from ..database import get_db

router = APIRouter(
    prefix="/vote",
    tags=["Votes"]
)       

@router.post("", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_db), 
         current_user: models.User = Depends(oauth2.get_current_user)):
    
    post=db.query(models.Post).filter(models.Post.id == vote.post_id).first() 
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f"post with id {vote.post_id} does not exist")

    if vote.dir == 1:  
        # Check if the user has already voted for the post
        vote_query = db.query(models.Vote).filter(
            models.Vote.post_id == vote.post_id,
            models.Vote.user_id == current_user.id
        )
        found_vote = vote_query.first()
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="You have already voted for this post")
        
        # Create a new vote
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id) #this adds a new row to the votes table
        db.add(new_vote)
        db.commit()
        return {"message": "Successfully added vote"}
    else:  # vote.dir==0 Remove vote  
        vote_query = db.query(models.Vote).filter(
            models.Vote.post_id == vote.post_id,
            models.Vote.user_id == current_user.id
        )
        found_vote = vote_query.first()
        if not found_vote: # ie if found_vote is None, therefore no vote to delete253
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Vote does not exist")
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Successfully removed vote"}  

