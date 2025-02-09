from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from api.config.env import get_session
from api.models.models import Customer
from typing import List

router = APIRouter(prefix="/customers", tags=["customers"])

# Get All Customers with Pagination
@router.get("/", response_model=List[Customer])
def get_customers(
    session: Session = Depends(get_session),
    offset: int = Query(0, description="Number of records to skip"),
    limit: int = Query(10, description="Maximum number of records to return (max 100)", le=100)
):
    customers = session.exec(select(Customer).offset(offset).limit(limit)).all()
    if not customers:
        raise HTTPException(status_code=404, detail="No customers found")
    return customers

# Get Customer by ID
@router.get("/{customer_id}", response_model=Customer)
def get_customer(customer_id: int, session: Session = Depends(get_session)):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

# Create a Customer
@router.post("/", response_model=Customer)
def create_customer(customer: Customer, session: Session = Depends(get_session)):
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

# Update a Customer
@router.put("/{customer_id}", response_model=Customer)
def update_customer(customer_id: int, customer_data: Customer, session: Session = Depends(get_session)):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    customer_dict = customer_data.dict(exclude_unset=True)
    for key, value in customer_dict.items():
        setattr(customer, key, value)

    session.commit()
    session.refresh(customer)
    return customer

# Delete a Customer
@router.delete("/{customer_id}")
def delete_customer(customer_id: int, session: Session = Depends(get_session)):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    session.delete(customer)
    session.commit()
    return {"message": "Customer deleted successfully"}