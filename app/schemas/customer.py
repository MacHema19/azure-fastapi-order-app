from pydantic import BaseModel, Field


class CustomerCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., min_length=5, max_length=30)
    address: str = Field(..., min_length=3, max_length=255)


class CustomerResponse(BaseModel):
    id: int
    name: str
    phone: str
    address: str

    model_config = {
        "from_attributes": True
    }
