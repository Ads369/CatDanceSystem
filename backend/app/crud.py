from sqlmodel import Session, select

from .models import Dancer


def create_dancer(session: Session, dancer: Dancer):
    db_dancer = Dancer.from_orm(dancer)
    session.add(db_dancer)
    session.commit()
    session.refresh(db_dancer)
    return db_dancer


def get_dancers(session: Session):
    return session.exec(select(Dancer)).all()


def get_dancer(session: Session, dancer_id: int):
    return session.get(Dancer, dancer_id)


def delete_dancer(session: Session, dancer_id: int):
    dancer = session.get(Dancer, dancer_id)
    if dancer:
        session.delete(dancer)
        session.commit()
        return True
    return False
