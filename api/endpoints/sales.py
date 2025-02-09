from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from datetime import datetime
from api.config.env import get_session
from api.models.models import Sale
from typing import List

router = APIRouter(prefix="/sales", tags=["sales"])

@router.get("/", response_model=List[Sale])
def get_sales(session: Session = Depends(get_session), offset: int = 0, limit: int = 10):
    return session.exec(select(Sale).offset(offset).limit(limit)).all()

@router.get("/{order_number}/{line_item}", response_model=Sale)
def get_sale(order_number: int, line_item: int, session: Session = Depends(get_session)):
    sale = session.get(Sale, (order_number, line_item))
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

@router.post("/", response_model=Sale)
def create_sale(sale: Sale, session: Session = Depends(get_session)):
    if isinstance(sale.OrderDate, str):
        sale.OrderDate = datetime.strptime(sale.OrderDate, "%Y-%m-%d").date()
    if isinstance(sale.DeliveryDate, str):
        sale.DeliveryDate = datetime.strptime(sale.DeliveryDate, "%Y-%m-%d").date()
    
    session.add(sale)
    session.commit()
    session.refresh(sale)
    return sale

@router.delete("/{order_number}/{line_item}")
def delete_sale(order_number: int, line_item: int, session: Session = Depends(get_session)):
    sale = session.get(Sale, (order_number, line_item))
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")

    session.delete(sale)
    session.commit()
    return {"message": "Sale deleted successfully"}