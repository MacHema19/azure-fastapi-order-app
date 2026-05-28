from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.customer import Customer
from app.models.menu import MenuItem
from app.models.order import Order, OrderItem
from app.schemas.order import OrderCreate, OrderStatusUpdate


def create_order(db: Session, order_data: OrderCreate):
    customer = db.query(Customer).filter(Customer.id == order_data.customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    if not order_data.items:
        raise HTTPException(status_code=400, detail="Order must contain at least one item")

    order = Order(customer_id=order_data.customer_id)
    total_amount = 0.0

    for item in order_data.items:
        menu_item = db.query(MenuItem).filter(MenuItem.id == item.menu_item_id).first()

        if not menu_item:
            raise HTTPException(
                status_code=404,
                detail=f"Menu item with id {item.menu_item_id} not found"
            )

        if not menu_item.is_available:
            raise HTTPException(
                status_code=400,
                detail=f"Menu item '{menu_item.name}' is not available"
            )

        subtotal = menu_item.price * item.quantity
        total_amount += subtotal

        order.items.append(
            OrderItem(
                menu_item_id=menu_item.id,
                quantity=item.quantity,
                unit_price=menu_item.price,
                subtotal=subtotal,
            )
        )

    order.total_amount = total_amount

    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def get_orders(db: Session):
    return db.query(Order).all()


def get_order_by_id(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


def update_order_status(db: Session, order_id: int, update_data: OrderStatusUpdate):
    order = get_order_by_id(db, order_id)
    order.status = update_data.status.value
    db.commit()
    db.refresh(order)
    return order
