from pydantic import BaseModel, Field, model_validator, ConfigDict
from typing import Optional
from datetime import datetime


class BlogCreate(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @model_validator(mode="before")
    def generate_slug(cls, values):
        if 'title' in values:
            values['slug'] = values.get("title").replace(" ", "-").lower()
        return values
    

class ShowBlog(BaseModel):
    title: str
    content: Optional[str] = None
    create_at: datetime

    # class Config():
    #     orm_mode = True
    model_config = ConfigDict(from_attributes=True)


class BlogUpdate(BlogCreate):
    pass