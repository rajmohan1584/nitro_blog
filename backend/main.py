from datetime import datetime, timezone
from typing import Annotated

import models
from database import Base, engine, get_db
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from schemas import (
    PostCreate,
    PostPatch,
    PostResponse,
    UserCreate,
    UserPatch,
    UserResponse,
)
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3999"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

# posts: list[dict] = [
#     {
#         "id": 1,
#         "author": "Raj",
#         "title": "FastAPI is Awesome",
#         "content": "This framework is really easy to use and super fast.",
#         "date_posted": "April 20, 2025",
#     },
#     {
#         "id": 2,
#         "author": "King Mohan",
#         "title": "Python is Great for Web Development",
#         "content": "Python is a great language for web development, and FastAPI makes it even...",
#         "date_posted": "April 21, 2025",
#     },
# ]

###########################################################################
# HOME / TEST ROUTES
###########################################################################
@app.get("/home_json", response_class=JSONResponse, include_in_schema=False)
def home_json() -> JSONResponse:
    return {"message": "Hello, FastAPI Nitro Blog!"}


@app.get("/home", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request, "home.html", {"posts": "posts", "title": "Home"}
    )


@app.get("/html", response_class=HTMLResponse, include_in_schema=False)
def html_response() -> HTMLResponse:
    return HTMLResponse(content="<h1>Hello, FastAPI Nitro Blog!</h1>", status_code=200)



###########################################################################
# User routes
###########################################################################
@app.post("/users", response_model=UserResponse)
def create_user(
    user: UserCreate, db: Annotated[Session, Depends(get_db)]
) -> UserResponse:
    result = db.execute(select(models.User).where(models.User.username == user.username))
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    result = db.execute(select(models.User).where(models.User.email == user.email))
    existing_email = result.scalars().first()

    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = models.User(username=user.username, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users", response_model=list[UserResponse])
def get_users(db: Annotated[Session, Depends(get_db)]) -> list[UserResponse]:
    result = db.execute(select(models.User))
    users = result.scalars().all()
    return users

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Annotated[Session, Depends(get_db)]) -> UserResponse:
    result = db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return user

@app.patch("/users/{user_id}", response_model=UserResponse)
def patch_user(user_id: int, user_data: UserPatch, db: Annotated[Session, Depends(get_db)]) -> UserResponse:
    result = db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    if (user_data.username is not None and user_data.username != user.username):
        result = db.execute(select(models.User).where(models.User.username == user_data.username))
        existing_user = result.scalars().first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

    if (user_data.email is not None and user_data.email != user.email):
        result = db.execute(select(models.User).where(models.User.email == user_data.email))
        existing_email = result.scalars().first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already exists")

    if user_data.username is not None:
        user.username = user_data.username
    if user_data.email is not None:
        user.email = user_data.email
    if user_data.image_file is not None:
        user.image_file = user_data.image_file

    db.commit()
    db.refresh(user)

    return user

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    db.delete(user)
    db.commit()

@app.get("/users/{user_id}/posts", response_model=list[PostResponse])
def get_user_posts(user_id: int, db: Annotated[Session, Depends(get_db)]) -> list[PostResponse]:
    result = db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    result = db.execute(select(models.Post).where(models.Post.user_id == user_id))
    posts = result.scalars().all()

    return posts


###########################################################################
# Post routes
###########################################################################
@app.get("/posts", response_model=list[PostResponse])
def get_posts(request: Request, db: Annotated[Session, Depends(get_db)]) -> list[PostResponse]:
    result = db.execute(select(models.Post))
    posts = result.scalars().all()
    return posts

@app.get("/posts/{post_id}", response_model=PostResponse)
def get_post(
    request: Request, post_id: int, db: Annotated[Session, Depends(get_db)]
) -> PostResponse:
    result = db.execute(select(models.Post).where(models.Post.id == post_id))
    post = result.scalars().first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} not found")
    return post

@app.post("/posts", response_model=PostResponse)
def create_post(post: PostCreate, db: Annotated[Session, Depends(get_db)]) -> PostResponse:
    result = db.execute(select(models.User).where(models.User.id == post.user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {post.user_id} not found")

    new_post = models.Post(title=post.title, content=post.content, user_id=user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@app.put("/posts/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post_data: PostCreate, db: Annotated[Session, Depends(get_db)]) -> PostResponse:
    result = db.execute(select(models.Post).where(models.Post.id == post_id))
    post = result.scalars().first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} not found")

    result = db.execute(select(models.User).where(models.User.id == post_data.user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=404, detail=f"User with id {post_data.user_id} not found"
        )

    post.user_id = user.id
    post.title = post_data.title
    post.content = post_data.content
    post.date_posted = datetime.now(timezone.utc)
    
    db.commit()
    db.refresh(post)
    return post

@app.patch("/posts/{post_id}", response_model=PostResponse)
def patch_post(
    post_id: int, post_data: PostPatch, db: Annotated[Session, Depends(get_db)]
) -> PostResponse:
    result = db.execute(select(models.Post).where(models.Post.id == post_id))
    post = result.scalars().first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} not found")
    
    update_data = post_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(post, field, value)

    post.date_posted = datetime.now(timezone.utc)

    db.commit()
    db.refresh(post)
    return post

@app.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.Post).where(models.Post.id == post_id))
    post = result.scalars().first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} not found")
    db.delete(post)
    db.commit()

###########################################################################
# Post routes OLD
###########################################################################
# @app.get("/posts", response_model=list[PostResponse])
# def get_posts() -> list[PostResponse]:
#     return [PostResponse.model_validate(post) for post in posts]


# @app.get("/posts/{post_id}", response_model=PostResponse)
# def get_post(request: Request, post_id: int) -> PostResponse:
#     post = next((post for post in posts if post["id"] == post_id), None)
#     if post:
#         return PostResponse.model_validate(post)
#     else:
#         raise HTTPException(status_code=404, detail="Post not found")


# @app.post("/posts", response_model=PostResponse)
# def create_post(request: Request, post: PostCreate) -> PostResponse:
#     new_id = max(post["id"] for post in posts) + 1 if posts else 1
#     new_post = PostResponse(
#         id=new_id,
#         title=post.title,
#         content=post.content,
#         author=post.author,
#         date_posted=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
#     )
#     posts.append(new_post.to_dict())
#     return new_post
