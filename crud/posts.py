from schemas.posts import PostUpdate, PostCreate
from sqlalchemy.orm import Session
from models import Post


def create_post(session: Session, schema: PostCreate):
    post = Post(**schema.model_dump())
    session.add(post)
    session.commit()
    session.refresh(post)
    return post


def get_all_posts(session: Session):
    return session.query(Post).all()


def get_post_by_id(session: Session, post_id: int):
    return session.query(Post).filter_by(id=post_id).first()


def update_post_by_id(session: Session, post_id: int, post_data: PostUpdate | dict):
    db_post = session.query(Post).filter_by(id=post_id).first()

    if db_post:
        for key, value in (post_data if isinstance(post_data, dict) else post_data.model_dump()).items():
            if hasattr(db_post, key):
                setattr(db_post, key, value)
        session.commit()
        session.refresh(db_post)
    return db_post


def delete_post_by_id(session: Session, post_id: int):
    post = session.query(Post).filter_by(id=post_id).first()
    if post:
        session.delete(post)
        session.commit()
        return post
