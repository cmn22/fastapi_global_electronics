from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from api.config.env import get_session
from api.models.models import Product
from typing import List

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=List[Product])
def get_products(session: Session = Depends(get_session), offset: int = 0, limit: int = 10):
    return session.exec(select(Product).offset(offset).limit(limit)).all()

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=Product)
def create_product(product: Product, session: Session = Depends(get_session)):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product_data: Product, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product_dict = product_data.dict(exclude_unset=True)
    for key, value in product_dict.items():
        setattr(product, key, value)

    session.commit()
    session.refresh(product)
    return product

@router.delete("/{product_id}")
def delete_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    session.delete(product)
    session.commit()
    return {"message": "Product deleted successfully"}