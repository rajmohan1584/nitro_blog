# from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PostBase(BaseModel):
    title: str = Field(
        min_length=1, max_length=100, description="The title of the post"
    )
    content: str = Field(min_length=1, description="The content of the post")
    author: str = Field(min_length=1, description="The author of the post")

    model_config = ConfigDict(extra="forbid")

    def to_dict(self) -> dict:
        return self.model_dump()


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., description="The ID of the post")
    date_posted: str = Field(..., description="The date the post was posted")
