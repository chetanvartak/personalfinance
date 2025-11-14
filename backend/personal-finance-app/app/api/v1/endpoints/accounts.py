from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.account import AccountOut, AccountCreate, AccountUpdate
from app.core.database import get_db
from app.repositories.account_repository import AccountRepository

router = APIRouter()


@router.get('/', response_model=List[AccountOut])
def list_accounts(db=Depends(get_db)):
    repo = AccountRepository(db)
    return repo.list_all()


@router.get('/{account_id}', response_model=AccountOut)
def get_account(account_id: int, db=Depends(get_db)):
    repo = AccountRepository(db)
    account = repo.get(account_id)
    if account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Account not found')
    return account


@router.post('/', response_model=AccountOut, status_code=status.HTTP_201_CREATED)
def create_account(payload: AccountCreate, db=Depends(get_db)):
    repo = AccountRepository(db)
    account = repo.create(payload)
    return account


@router.put('/{account_id}', response_model=AccountOut)
def update_account(account_id: int, payload: AccountUpdate, db=Depends(get_db)):
    repo = AccountRepository(db)
    account = repo.get(account_id)
    if account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Account not found')
    updates = payload.dict(exclude_unset=True)
    updated = repo.update(account, updates)
    return updated


@router.delete('/{account_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_account(account_id: int, db=Depends(get_db)):
    repo = AccountRepository(db)
    account = repo.get(account_id)
    if account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Account not found')
    repo.delete(account)
    return None
