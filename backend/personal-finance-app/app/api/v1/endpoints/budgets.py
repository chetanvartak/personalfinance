from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def list_budgets():
    return [{"id": 1, "name": "Monthly"}]
