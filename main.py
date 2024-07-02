from fastapi import FastAPI
from typing import  Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit=10,published:bool=True, sort: Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs from the bloglist'}
    else:
        return {'data':f'{limit} Unpublished blogs from the bloglist'}
        


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}
    # return {'data':{'name':"Ifeoluwa"},'School':{'primary':'Sundora','secondary':'Nut Model college'}}



@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{1,2}}

class Blog(BaseModel):
    title : str
    body : str 
    published : Optional[bool]


@app.post('/blog')
def create_blog(request:Blog):
    return {'data':f'Blog is created with {request.title}'}


# if __name__ == "__main__":
#     print("Starting Uvicorn on port 9000...")
#     uvicorn.run(app, host="127.0.0.1", port=9000)