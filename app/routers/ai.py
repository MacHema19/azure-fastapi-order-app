from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.order_agent import handle_order_message

router = APIRouter(prefix="/ai", tags=["AI Order Assistant"])


class ChatRequest(BaseModel):
    message: str
    customer_id: int | None = None


@router.post("/chat")
def chat_with_order_agent(request: ChatRequest):
    response = handle_order_message(
        message=request.message,
        customer_id=request.customer_id
    )
    return {"response": response}