from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

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


@app.get("/")
def home() -> JSONResponse:
    return {"message": "Hello, FastAPI Nitro Blog!"}


@app.get("/html", response_class=HTMLResponse, include_in_schema=False)
def html_response() -> HTMLResponse:
    return HTMLResponse(content="<h1>Hello, FastAPI Nitro Blog!</h1>", status_code=200)


@app.get("/posts", response_class=JSONResponse)
def get_posts() -> JSONResponse:
    return {"data": posts}
