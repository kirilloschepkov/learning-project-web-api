from typing import List, Union

from fastapi import APIRouter, Depends

from database import get_db
from routes.manager import notify_clients
from schemas.posts import Post, PostUpdate, PostCreate
from sqlalchemy.orm import Session

from crud.posts import (
    create_post,
    get_all_posts,
    get_post_by_id,
    update_post_by_id,
    delete_post_by_id
)

router_posts = APIRouter(prefix='/posts', tags=['post'])


@router_posts.post("/", response_model=Post)
async def create_post_route(schema: PostCreate, db: Session = Depends(get_db)):
    new_post = create_post(db, schema)
    await notify_clients(f"Пост добавлен")
    return new_post


@router_posts.get("/", response_model=List[Post])
async def get_all_posts_route(db: Session = Depends(get_db)):
    return get_all_posts(db)


@router_posts.get("/{post_id}", response_model=Union[Post, dict])
async def get_post_by_id_route(post_id: int, db: Session = Depends(get_db)):
    post = get_post_by_id(db, post_id)
    if post:
        return post
    print(post)
    return {"message": "Пост не найдет"}


@router_posts.patch("/{post_id}", response_model=Union[Post, dict])
async def update_post_by_id_route(post_id: int, schema: PostUpdate, db: Session = Depends(get_db)):
    post = update_post_by_id(db, post_id, schema)
    if post:
        await notify_clients(f"Пост с ID{post_id} изменен")
        return post
    return {"message": "Пост не найдет"}


@router_posts.delete("/{post_id}", response_model=Union[Post, dict])
async def delete_post_by_id_route(post_id: int, db: Session = Depends(get_db)):
    post = delete_post_by_id(db, post_id)
    if post:
        await notify_clients(f"Пост с ID{post.id} удален")
        return post
    return {"message": "Пост не найдет"}
