from fastapi import FastAPI
from . import  models 
from .database import engine
from .routers import blog,user, authentication


app = FastAPI()

@app.get("/")
async def homepage():
    return {
        "details":"Homepage Success"
        }

    
models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)





