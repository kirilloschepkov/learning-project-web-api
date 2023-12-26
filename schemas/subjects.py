from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class SubjectBase(BaseModel):
    name: str


class SubjectCreate(SubjectBase):
    pass


class SubjectUpdate(SubjectBase):
    name: Optional[str] = None


class Subject(SubjectBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
