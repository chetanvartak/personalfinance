from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI(title="Personal Finance API")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"status": "personal-finance-app running"}
