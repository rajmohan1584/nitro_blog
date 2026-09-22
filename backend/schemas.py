# from typing import Optional

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50, description="The username of the user")
    email: EmailStr = Field(max_length=120,description="The email of the user")

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., description="The ID of the user")
    image_file: str | None = Field(default=None, description="The image file of the user")
    image_path: str = Field(..., description="The image path of the user")

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100, description="The title of the post")
    content: str = Field(min_length=1, description="The content of the post")
    author: str = Field(min_length=1, description="The author of the post")

    model_config = ConfigDict(extra="forbid")

    def to_dict(self) -> dict:
        return self.model_dump()


class PostCreate(PostBase):
    user_id: int = Field(..., description="The ID of the user (TODO: Get from Session)")


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., description="The ID of the post")
    user_id: int = Field(..., description="The ID of the user (TODO: Same as author.id)")
    date_posted: datetime = Field(..., description="The date the post was posted")
    author: UserResponse = Field(..., description="The author of the post")
