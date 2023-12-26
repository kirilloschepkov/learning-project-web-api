from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    posts = relationship('Post', back_populates='subject')
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    subject = relationship('Subject', back_populates='posts')
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())
