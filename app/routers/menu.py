from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.menu import MenuItemCreate, MenuItemResponse, MenuAvailabilityUpdate
from app.services import menu_service

router = APIRouter(prefix="/menu", tags=["Menu"])


@router.post("", response_model=MenuItemResponse)
def create_menu_item(menu_data: MenuItemCreate, db: Session = Depends(get_db)):
    return menu_service.create_menu_item(db, menu_data)


@router.get("", response_model=list[MenuItemResponse])
def get_menu_items(db: Session = Depends(get_db)):
    return menu_service.get_menu_items(db)


@router.get("/{menu_item_id}", response_model=MenuItemResponse)
def get_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return menu_service.get_menu_item_by_id(db, menu_item_id)


@router.patch("/{menu_item_id}/availability", response_model=MenuItemResponse)
def update_menu_availability(
    menu_item_id: int,
    update_data: MenuAvailabilityUpdate,
    db: Session = Depends(get_db),
):
    return menu_service.update_menu_availability(db, menu_item_id, update_data)
