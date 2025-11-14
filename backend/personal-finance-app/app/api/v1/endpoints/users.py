from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.user import UserCreate, UserOut
from app.repositories.user_repository import UserRepository
from app.core.database import get_db

router = APIRouter()

@router.post('/', response_model=UserOut)
def create_user(payload: UserCreate, db=Depends(get_db)):
    repo = UserRepository(db)
    user = repo.create(payload)
    return user

@router.get('/', response_model=List[UserOut])
def list_users(db=Depends(get_db)):
    repo = UserRepository(db)
    return repo.list_all()


@router.get('/{user_id}', response_model=UserOut)
def get_user(user_id: int, db=Depends(get_db)):
    repo = UserRepository(db)
    user = repo.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@router.put('/{user_id}', response_model=UserOut)
def update_user(user_id: int, payload: UserCreate, db=Depends(get_db)):
    repo = UserRepository(db)
    user = repo.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    updates = payload.dict(exclude_unset=True)
    updated = repo.update(user, updates)
    return updated


@router.delete('/{user_id}', status_code=204)
def delete_user(user_id: int, db=Depends(get_db)):
    repo = UserRepository(db)
    user = repo.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    repo.delete(user)
    return None
