from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from schemas import PostCreate, PostResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Raj",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "King Mohan",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even...",
        "date_posted": "April 21, 2025",
    },
]


@app.get("/home_json", response_class=JSONResponse, include_in_schema=False)
def home_json() -> JSONResponse:
    return {"message": "Hello, FastAPI Nitro Blog!"}


@app.get("/home", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Home"}
    )


@app.get("/html", response_class=HTMLResponse, include_in_schema=False)
def html_response() -> HTMLResponse:
    return HTMLResponse(content="<h1>Hello, FastAPI Nitro Blog!</h1>", status_code=200)


@app.get("/posts", response_model=list[PostResponse])
def get_posts() -> list[PostResponse]:
    return [PostResponse.model_validate(post) for post in posts]


@app.get("/posts/{post_id}", response_model=PostResponse)
def get_post(request: Request, post_id: int) -> PostResponse:
    post = next((post for post in posts if post["id"] == post_id), None)
    if post:
        return PostResponse.model_validate(post)
    else:
        raise HTTPException(status_code=404, detail="Post not found")


@app.post("/posts", response_model=PostResponse)
def create_post(request: Request, post: PostCreate) -> PostResponse:
    new_id = max(post["id"] for post in posts) + 1 if posts else 1
    new_post = PostResponse(
        id=new_id,
        title=post.title,
        content=post.content,
        author=post.author,
        date_posted=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
    )
    posts.append(new_post.to_dict())
    return new_post
