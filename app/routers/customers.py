from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.customer import CustomerCreate, CustomerResponse
from app.services import customer_service

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("", response_model=CustomerResponse)
def create_customer(customer_data: CustomerCreate, db: Session = Depends(get_db)):
    return customer_service.create_customer(db, customer_data)


@router.get("", response_model=list[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    return customer_service.get_customers(db)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    return customer_service.get_customer_by_id(db, customer_id)
