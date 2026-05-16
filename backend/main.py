from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

posts = [
    {
        "id":1,
        "title":"FastAPI is Awesome",
        "content": "FastAPI is a python backend framework that makes it very easy for you to deploy your app.",
        "author":"Dev",
        "date_posted": "May 16 2026" 
    },
    {
        "id": 2,
        "title":"I love popcorns",
        "content": "Popcorns are my favourite snack and I love to have them while watching a show or a movie.",
        "author":"Cloud",
        "date_posted": "May 16 2026"
    }
]

app = FastAPI() 

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
@app.get("/posts")
def root(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts":posts, "title": "Home"})

@app.post("/api/posts")
def posts_api():
    return posts
