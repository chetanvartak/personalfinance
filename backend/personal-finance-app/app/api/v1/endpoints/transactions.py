from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.transaction import TransactionOut, TransactionCreate
from app.core.database import get_db
from app.repositories.transaction_repository import TransactionRepository

router = APIRouter()

@router.get('/', response_model=List[TransactionOut])
def list_transactions(db=Depends(get_db)):
    repo = TransactionRepository(db)
    return repo.list_all()


@router.get('/{transaction_id}', response_model=TransactionOut)
def get_transaction(transaction_id: int, db=Depends(get_db)):
    repo = TransactionRepository(db)
    tx = repo.get(transaction_id)
    if tx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Transaction not found')
    return tx


@router.post('/', response_model=TransactionOut)
def create_transaction(payload: TransactionCreate, db=Depends(get_db)):
    repo = TransactionRepository(db)
    tx = repo.create(payload)
    return tx


@router.put('/{transaction_id}', response_model=TransactionOut)
def update_transaction(transaction_id: int, payload: TransactionCreate, db=Depends(get_db)):
    repo = TransactionRepository(db)
    tx = repo.get(transaction_id)
    if tx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Transaction not found')
    updates = payload.dict(exclude_unset=True)
    updated = repo.update(tx, updates)
    return updated


@router.delete('/{transaction_id}', status_code=204)
def delete_transaction(transaction_id: int, db=Depends(get_db)):
    repo = TransactionRepository(db)
    tx = repo.get(transaction_id)
    if tx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Transaction not found')
    repo.delete(tx)
    return None
