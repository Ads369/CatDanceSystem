# backend/app/api/dancers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ..crud import create_dancer, delete_dancer, get_dancer, get_dancers
from ..database import get_session
from ..models import Dancer, DancerCreate, DancerRead

router = APIRouter()


@router.post("/dancers/", response_model=DancerRead)
def create_dancer_endpoint(
    dancer: DancerCreate, session: Session = Depends(get_session)
):
    return create_dancer(session, dancer)


@router.get("/dancers/", response_model=list[DancerRead])
def read_dancers(session: Session = Depends(get_session)):
    return get_dancers(session)


@router.get("/dancers/{dancer_id}", response_model=DancerRead)
def read_dancer(dancer_id: int, session: Session = Depends(get_session)):
    dancer = get_dancer(session, dancer_id)
    if not dancer:
        raise HTTPException(status_code=404, detail="Dancer not found")
    return dancer


@router.delete("/dancers/{dancer_id}")
def delete_dancer_endpoint(dancer_id: int, session: Session = Depends(get_session)):
    if not delete_dancer(session, dancer_id):
        raise HTTPException(status_code=404, detail="Dancer not found")
    return {"message": "Dancer deleted"}
