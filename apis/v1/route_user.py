from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schemas.user import UserCreate, ShowUser
from db.session import get_db
from db.repository.user import create_new_user

router = APIRouter()

@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session=Depends(get_db)): # validate user and get db session
    user = create_new_user(user=user, db=db) # perform operation on db
    return user # return user in the ShowUser