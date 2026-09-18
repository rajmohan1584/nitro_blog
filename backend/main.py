from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
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


@app.get("/posts", response_class=JSONResponse)
def get_posts() -> JSONResponse:
    return {"data": posts}
