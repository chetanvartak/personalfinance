from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.category import CategoryOut
from app.schemas.category import CategoryCreate
from app.core.database import get_db
from app.repositories.category_repository import CategoryRepository

router = APIRouter()


@router.get('/', response_model=List[CategoryOut])
def list_categories(db=Depends(get_db)):
    repo = CategoryRepository(db)
    return repo.list_all()


@router.post('/', response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
def create_category(payload: CategoryCreate, db=Depends(get_db)):
    repo = CategoryRepository(db)
    cat = repo.create(payload)
    return cat


@router.get('/{category_id}', response_model=CategoryOut)
def get_category(category_id: int, db=Depends(get_db)):
    repo = CategoryRepository(db)
    cat = repo.get(category_id)
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category not found')
    return cat


@router.put('/{category_id}', response_model=CategoryOut)
def update_category(category_id: int, payload: CategoryCreate, db=Depends(get_db)):
    repo = CategoryRepository(db)
    cat = repo.get(category_id)
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category not found')
    updates = payload.dict(exclude_unset=True)
    updated = repo.update(cat, updates)
    return updated


@router.delete('/{category_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db=Depends(get_db)):
    repo = CategoryRepository(db)
    cat = repo.get(category_id)
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category not found')
    repo.delete(cat)
    return None
