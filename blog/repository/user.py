from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from ..import models,schemas
from ..hashing import Hash



def create(request:schemas.User,db:Session):
  new_users = models.User(
    name = request.name,
    email = request.email,
    password = Hash.bcrypt(request.password)
    )
  db.add(new_users)
  db.commit()
  db.refresh(new_users)
  return new_users


def get_user(id,db:Session):
  user = db.query(models.User).filter(models.User.id==id).first()
  if not user:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"User with id {id} does not exist")
  return user 