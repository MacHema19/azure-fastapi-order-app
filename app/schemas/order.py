from pydantic import BaseModel, Field
from app.models.order import OrderStatus


class OrderItemCreate(BaseModel):
    menu_item_id: int
    quantity: int = Field(..., gt=0)


class OrderCreate(BaseModel):
    customer_id: int
    items: list[OrderItemCreate]


class OrderItemResponse(BaseModel):
    id: int
    menu_item_id: int
    quantity: int
    unit_price: float
    subtotal: float

    model_config = {
        "from_attributes": True
    }


class OrderResponse(BaseModel):
    id: int
    customer_id: int
    status: str
    total_amount: float
    items: list[OrderItemResponse]

    model_config = {
        "from_attributes": True
    }


class OrderStatusUpdate(BaseModel):
    status: OrderStatus
