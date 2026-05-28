from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.menu import MenuItem
from app.schemas.menu import MenuItemCreate, MenuAvailabilityUpdate


def create_menu_item(db: Session, menu_data: MenuItemCreate):
    menu_item = MenuItem(**menu_data.model_dump())
    db.add(menu_item)
    db.commit()
    db.refresh(menu_item)
    return menu_item


def get_menu_items(db: Session):
    return db.query(MenuItem).all()


def get_menu_item_by_id(db: Session, menu_item_id: int):
    menu_item = db.query(MenuItem).filter(MenuItem.id == menu_item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return menu_item


def update_menu_availability(db: Session, menu_item_id: int, update_data: MenuAvailabilityUpdate):
    menu_item = get_menu_item_by_id(db, menu_item_id)
    menu_item.is_available = update_data.is_available
    db.commit()
    db.refresh(menu_item)
    return menu_item
