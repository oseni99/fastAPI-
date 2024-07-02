from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from fastapi import  Depends
from ..import models,schemas
from ..database import get_db



def get_all(db:Session = Depends(get_db)):
  blogs = db.query(models.Blog).all()
  return blogs 

def create(request:schemas.Blog,db:Session = Depends(get_db)):
  new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog

def destroy(id:int,db:Session = Depends(get_db)):
  blog = db.query(models.Blog).filter(models.Blog.id == id).first()
  if not blog:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
  db.delete(blog)
  db.commit()
  return {'detail':'The blog is deleted'}

def update(id:int,request:schemas.Blog,db:Session):
  blog = db.query(models.Blog).filter(models.Blog.id == id)
  if not blog.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
  blog.update(request.model_dump(exclude_unset=True))
  db.commit()
  return {'detail':'Updated Succesfully'}

def show(id:int,db:Session):
  blog = db.query(models.Blog).filter(models.Blog.id == id).first()
  if not blog:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Blog with id {id} is not availaible")
  return blog 