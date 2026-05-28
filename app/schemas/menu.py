from pydantic import BaseModel, Field


class MenuItemCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str | None = None
    price: float = Field(..., gt=0)


class MenuItemResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    is_available: bool

    model_config = {
        "from_attributes": True
    }


class MenuAvailabilityUpdate(BaseModel):
    is_available: bool
