from fastapi import APIRouter,Depends,HTTPException,status
from ..import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db
from ..hashing import Hash
from ..token import create_access_token
from ..schemas import Token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



router = APIRouter(
  tags=['Authentication'],
  )

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.email == request.username).first()
  if not user:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail="Invalid Credentials")
  elif not Hash.verify(user.password,request.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail="Invalid Credentials[Password]")
  # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  access_token = create_access_token(
        data={"sub": user.email}
    )
  return Token(access_token=access_token, token_type="bearer")