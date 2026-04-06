from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, expense
from app.routes import expense_routes

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(expense_routes.router)

@app.get("/")
def home():
    return {"message": "Expense Approval System is running "}