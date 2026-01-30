from fastapi import FastAPI
from app.routers.expense_router import router

app = FastAPI(title="Expense Tracker API")

app.include_router(router)
