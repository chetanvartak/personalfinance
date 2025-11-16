import codecs
from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, status, File
from typing import List, Optional
from app.schemas.transaction import TransactionListFiltered, TransactionOut, TransactionCreate
from app.core.database import get_db
from app.repositories.transaction_repository import TransactionRepository
from datetime import date, datetime
from app.services.transaction_service import TransactionService
from typing import IO
router = APIRouter()

@router.get('/all', response_model=List[TransactionOut])
def list_transactions(db=Depends(get_db)):
    repo = TransactionRepository(db)
    return repo.list_all()

@router.post('/search', response_model=List[TransactionOut])
def search_transactions(
    start_date: datetime,
    end_date: datetime,
    account_ids: Optional[List[int]] = None,
    category_ids: Optional[List[int]] = None,
    description: Optional[str] = None,
    db=Depends(get_db)
):
    repo = TransactionRepository(db)
    return repo.search(
        start_date=start_date,
        end_date=end_date,
        account_ids=account_ids,
        category_ids=category_ids,
        description=description
    )

@router.get('/id/{transaction_id}', response_model=TransactionOut)
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

@router.post("/accounts/{account_id}/import-csv", status_code=201)
def import_transactions_from_csv(
    account_id: int,
    file: UploadFile = File(...),
    db=Depends(get_db)
):
    """
    Endpoint to upload a CSV file of transactions for a specific account.
    """
    # Initialize dependencies
    repo = TransactionRepository(db)
    service = TransactionService(repo)
    
    # The service parses the file and prepares the data
    csv_reader = codecs.iterdecode(file.file, 'utf-8')
    #transactions_to_create = service.import_from_csv(csv_reader, account_id)

    # The service saves the prepared data using the repository's bulk method
    #created_transactions = service.save_imported_transactions(transactions_to_create)

    return {"message": f"Successfully imported len(transactions_to_create) transactions."}


@router.get("/filtered", response_model=TransactionListFiltered)
def list_filtered_transactions(
    page: int = Query(1, ge=1),
    page_size: int = Query(25, ge=1, le=100),
    sort_by: str = Query("date", regex="^(date|amount|account_name|category)$"),
    sort_order: str = Query("desc", regex="^(asc|desc)$"),
    search: Optional[str] = None,
    account_id: Optional[int] = None,
    category_id: Optional[int] = None,
    date_from: Optional[datetime] = None,
    date_to: Optional[datetime] = None,
    db=Depends(get_db)
):
    repo = TransactionRepository(db)
    return repo.list_filtered_transactions(
        page=page,
        page_size=page_size,
        sort_by=sort_by,
        sort_order=sort_order,
        search=search,
        account_id=account_id,
        category_id=category_id,
        date_from=date_from,
        date_to=date_to
    )    

