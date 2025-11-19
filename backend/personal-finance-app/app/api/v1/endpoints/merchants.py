import codecs
import csv
import io
from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, status, File
from typing import List, Optional
from app.schemas.merchant import MerchantListFiltered, MerchantOut, MerchantCreate, MerchantUpdate
from app.core.database import get_db
from app.repositories.merchant_repository import MerchantRepository
from datetime import date, datetime
from typing import IO
from datetime import date, datetime

from typing import IO
router = APIRouter()

@router.get('/all', response_model=List[MerchantOut])
def list_transactions(db=Depends(get_db)):
    repo = MerchantRepository(db)
    return repo.list_all()

@router.get('/id/{merchant_id}', response_model=MerchantOut)
def get_merchant(merchant_id: int, db=Depends(get_db)):
    repo = MerchantRepository(db)
    merchant = repo.get(merchant_id)
    if merchant is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Merchant not found')
    return merchant


@router.post('/', response_model=MerchantOut)
def create_merchant(payload: MerchantCreate, db=Depends(get_db)):
    repo = MerchantRepository(db)
    merchant = repo.create(payload)
    return merchant
@router.put('/{merchant_id}', response_model=MerchantOut)
def update_merchant(merchant_id: int, payload: MerchantUpdate, db=Depends(get_db)):
    repo = MerchantRepository(db)
    merchant = repo.get(merchant_id)
    if merchant is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Merchant not found')
    updates = payload.dict(exclude_unset=True)
    updated = repo.update(merchant, updates)
    return updated


@router.delete('/{merchant_id}', status_code=204)
def delete_merchant(merchant_id: int, db=Depends(get_db)):
    repo = MerchantRepository(db)
    merchant = repo.get(merchant_id)
    if merchant is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Merchant not found')
    repo.delete(merchant)
    return None

