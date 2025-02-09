from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from datetime import datetime
from api.config.env import get_session
from api.models.models import Customer
from typing import List

router = APIRouter(prefix="/customers", tags=["customers"])

@router.get("/", response_model=List[Customer])
def get_customers(session: Session = Depends(get_session), offset: int = 0, limit: int = 10):
    return session.exec(select(Customer).offset(offset).limit(limit)).all()

@router.get("/{customer_id}", response_model=Customer)
def get_customer(customer_id: int, session: Session = Depends(get_session)):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.post("/", response_model=Customer)
def create_customer(customer: Customer, session: Session = Depends(get_session)):
    if isinstance(customer.Birthday, str):
        customer.Birthday = datetime.strptime(customer.Birthday, "%Y-%m-%d").date()
    
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@router.put("/{customer_id}", response_model=Customer)
def update_customer(customer_id: int, customer_data: Customer, session: Session = Depends(get_session)):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    customer_dict = customer_data.dict(exclude_unset=True)

    if "Birthday" in customer_dict and isinstance(customer_dict["Birthday"], str):
        customer_dict["Birthday"] = datetime.strptime(customer_dict["Birthday"], "%Y-%m-%d").date()

    for key, value in customer_dict.items():
        setattr(customer, key, value)

    session.commit()
    session.refresh(customer)
    return customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, session: Session = Depends(get_session)):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    session.delete(customer)
    session.commit()
    return {"message": "Customer deleted successfully"}