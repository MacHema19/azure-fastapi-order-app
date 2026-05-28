from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.order import OrderCreate, OrderResponse, OrderStatusUpdate
from app.services import order_service

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("", response_model=OrderResponse)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    return order_service.create_order(db, order_data)


@router.get("", response_model=list[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return order_service.get_orders(db)


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return order_service.get_order_by_id(db, order_id)


@router.patch("/{order_id}/status", response_model=OrderResponse)
def update_order_status(
    order_id: int,
    update_data: OrderStatusUpdate,
    db: Session = Depends(get_db),
):
    return order_service.update_order_status(db, order_id, update_data)
