from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import customers, menu, orders

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Food Order Management API",
    description="Modular FastAPI backend for food ordering, menu, customers, and order tracking.",
    version="1.0.0",
)

app.include_router(customers.router)
app.include_router(menu.router)
app.include_router(orders.router)


@app.get("/")
def root():
    return {
        "message": "Food Order Management API is running",
        "docs": "/docs"
    }
