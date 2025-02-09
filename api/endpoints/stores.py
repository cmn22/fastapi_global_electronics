from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from datetime import datetime
from api.config.env import get_session
from api.models.models import Store
from typing import List

router = APIRouter(prefix="/stores", tags=["stores"])

@router.get("/", response_model=List[Store])
def get_stores(session: Session = Depends(get_session), offset: int = 0, limit: int = 10):
    return session.exec(select(Store).offset(offset).limit(limit)).all()

@router.get("/{store_id}", response_model=Store)
def get_store(store_id: int, session: Session = Depends(get_session)):
    store = session.get(Store, store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store

@router.post("/", response_model=Store)
def create_store(store: Store, session: Session = Depends(get_session)):
    if isinstance(store.OpenDate, str):
        store.OpenDate = datetime.strptime(store.OpenDate, "%Y-%m-%d").date()
    
    session.add(store)
    session.commit()
    session.refresh(store)
    return store

@router.delete("/{store_id}")
def delete_store(store_id: int, session: Session = Depends(get_session)):
    store = session.get(Store, store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")

    session.delete(store)
    session.commit()
    return {"message": "Store deleted successfully"}