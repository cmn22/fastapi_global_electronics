from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from datetime import datetime
from api.config.env import get_session
from api.models.models import ExchangeRate
from typing import List

router = APIRouter(prefix="/exchange-rates", tags=["exchange-rates"])

@router.get("/", response_model=List[ExchangeRate])
def get_exchange_rates(session: Session = Depends(get_session), offset: int = 0, limit: int = 10):
    return session.exec(select(ExchangeRate).offset(offset).limit(limit)).all()

@router.get("/{date}/{currency}", response_model=ExchangeRate)
def get_exchange_rate(date: str, currency: str, session: Session = Depends(get_session)):
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")

    exchange_rate = session.get(ExchangeRate, (parsed_date, currency))
    if not exchange_rate:
        raise HTTPException(status_code=404, detail="Exchange rate not found")
    
    return exchange_rate

@router.post("/", response_model=ExchangeRate)
def create_exchange_rate(exchange_rate: ExchangeRate, session: Session = Depends(get_session)):
    if isinstance(exchange_rate.Date, str):
        exchange_rate.Date = datetime.strptime(exchange_rate.Date, "%Y-%m-%d").date()
    
    session.add(exchange_rate)
    session.commit()
    session.refresh(exchange_rate)
    return exchange_rate

@router.put("/{date}/{currency}", response_model=ExchangeRate)
def update_exchange_rate(date: str, currency: str, exchange_rate_data: ExchangeRate, session: Session = Depends(get_session)):
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")

    exchange_rate = session.get(ExchangeRate, (parsed_date, currency))
    if not exchange_rate:
        raise HTTPException(status_code=404, detail="Exchange rate not found")

    exchange_rate_dict = exchange_rate_data.dict(exclude_unset=True)

    if "Date" in exchange_rate_dict and isinstance(exchange_rate_dict["Date"], str):
        exchange_rate_dict["Date"] = datetime.strptime(exchange_rate_dict["Date"], "%Y-%m-%d").date()

    for key, value in exchange_rate_dict.items():
        setattr(exchange_rate, key, value)

    session.commit()
    session.refresh(exchange_rate)
    return exchange_rate

@router.delete("/{date}/{currency}")
def delete_exchange_rate(date: str, currency: str, session: Session = Depends(get_session)):
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")

    exchange_rate = session.get(ExchangeRate, (parsed_date, currency))
    if not exchange_rate:
        raise HTTPException(status_code=404, detail="Exchange rate not found")

    session.delete(exchange_rate)
    session.commit()
    return {"message": "Exchange rate deleted successfully"}