from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.institution import InstitutionCreate, InstitutionOut
from app.repositories.institution_repository import InstitutionRepository
from app.core.database import get_db

router = APIRouter()


@router.get('/', response_model=List[InstitutionOut])
def list_institutions(db=Depends(get_db)):
    repo = InstitutionRepository(db)
    return repo.list_all()


@router.post('/', response_model=InstitutionOut, status_code=status.HTTP_201_CREATED)
def create_institution(payload: InstitutionCreate, db=Depends(get_db)):
    repo = InstitutionRepository(db)
    inst = repo.create(payload)
    return inst


@router.get('/{institution_id}', response_model=InstitutionOut)
def get_institution(institution_id: int, db=Depends(get_db)):
    repo = InstitutionRepository(db)
    inst = repo.get(institution_id)
    if inst is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Institution not found')
    return inst


@router.put('/{institution_id}', response_model=InstitutionOut)
def update_institution(institution_id: int, payload: InstitutionCreate, db=Depends(get_db)):
    repo = InstitutionRepository(db)
    inst = repo.get(institution_id)
    if inst is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Institution not found')
    updates = payload.dict(exclude_unset=True)
    updated = repo.update(inst, updates)
    return updated


@router.delete('/{institution_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_institution(institution_id: int, db=Depends(get_db)):
    repo = InstitutionRepository(db)
    inst = repo.get(institution_id)
    if inst is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Institution not found')
    repo.delete(inst)
    return None
