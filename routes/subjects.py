from typing import List, Union

from crud.subjects import create_subject, get_all_subjects, get_subject_by_id, update_subject_by_id, \
    delete_subject_by_id
from fastapi import APIRouter, Depends

from database import get_db
from routes.manager import notify_clients
from schemas.subjects import Subject, SubjectCreate, SubjectUpdate
from sqlalchemy.orm import Session


router_subjects = APIRouter(prefix='/subjects', tags=['subjects'])


@router_subjects.post("/", response_model=Subject)
async def create_subject_route_route(subject_data: SubjectCreate, db: Session = Depends(get_db)):
    subject = create_subject(db, subject_data)
    await notify_clients(f"Категория добавлена")
    return subject


@router_subjects.get("/", response_model=List[Subject])
async def get_all_subjects_route(db: Session = Depends(get_db)):
    return get_all_subjects(db)


@router_subjects.get("/{subject_id}", response_model=Union[Subject, dict])
async def get_subject_by_id_route(subject_id: int, db: Session = Depends(get_db)):
    subject = get_subject_by_id(db, subject_id)
    if subject:
        return subject
    return {"message": "Категория не найдена"}


@router_subjects.patch("/{subject_id}", response_model=Union[Subject, dict])
async def update_subject_by_id_route(subject_id: int, category_data: SubjectUpdate, db: Session = Depends(get_db)):
    subject = update_subject_by_id(db, subject_id, category_data)
    if subject:
        await notify_clients(f"Категория с ID{subject.id} изменена")
        return subject
    return {"message": "Категория не найдена"}


@router_subjects.delete("/{subject_id}", response_model=Union[Subject, dict])
async def delete_subject_by_id_route(subject_id: int, db: Session = Depends(get_db)):
    subject = delete_subject_by_id(db, subject_id)
    if subject:
        await notify_clients(f"Категория с ID{subject.id} удалена")
        return subject
    return {"message": "Категория не найдена"}
