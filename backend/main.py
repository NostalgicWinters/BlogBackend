from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"], 
    allow_headers=["*"],
)

class Author(BaseModel):
    id : int 
    name: str
    joined: date
    email: str

class Blogs(BaseModel):
    id: str = "000"
    title: str
    content: str
    author: Author

a = Author(id=1,name="Dev",joined=date(2001,12,4),email="SomeoneSomeone@gmail.com")
b = Blogs(id="001",title="Water", content="Water is very essential for our lives.", author=a )

blog_list = []


@app.get('/')
async def root():
    return {"message": "API Working"}

@app.get('/blogs')
async def show_blogs():
    return blog_list

@app.post('/write_blog')
async def write_blog(blog: Blogs):
    blog_list.append(blog.model_dump())
    return blog_list