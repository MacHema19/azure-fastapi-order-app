from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Food Order Management API"
    database_url: str = "sqlite:///./food_order.db"


settings = Settings()
