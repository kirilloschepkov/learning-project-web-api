from models import Subject
from schemas.subjects import SubjectCreate, SubjectUpdate
from sqlalchemy.orm import Session


def create_subject(session: Session, schema: SubjectCreate):
    new_subject = Subject(**schema.model_dump())
    session.add(new_subject)
    session.commit()
    session.refresh(new_subject)
    return new_subject


def get_all_subjects(session: Session):
    return session.query(Subject).all()


def get_subject_by_id(session: Session, subject_id: int):
    return session.query(Subject).filter_by(id=subject_id).first()


def update_subject_by_id(session: Session, subject_id: int, subject_data: SubjectUpdate | dict):
    subject = session.query(Subject).filter_by(id=subject_id).first()
    if subject:
        for key, value in (subject_data if isinstance(subject_data, dict) else subject_data.model_dump()).items():
            if hasattr(subject, key):
                setattr(subject, key, value)
        session.commit()
        session.refresh(subject)
    return subject


def delete_subject_by_id(session: Session, subject_id: int):
    subject = session.query(Subject).filter_by(id=subject_id).first()
    if subject:
        session.delete(subject)
        session.commit()
        return subject
