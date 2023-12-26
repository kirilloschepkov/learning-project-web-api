from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class PostBase(BaseModel):
    name: str
    subject_id: int


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    name: Optional[str] = None
    subject_id: Optional[int] = None


class Post(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
