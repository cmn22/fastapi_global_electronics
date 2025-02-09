from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Customer(SQLModel, table=True):
    __tablename__ = "Customers"
    CustomerKey: int = Field(primary_key=True)
    Name: str
    Gender: Optional[str] = None
    City: Optional[str] = None
    StateCode: Optional[str] = None
    State: Optional[str] = None
    ZipCode: Optional[str] = None
    Country: Optional[str] = None
    Continent: Optional[str] = None
    Birthday: Optional[date] = None

class Product(SQLModel, table=True):
    __tablename__ = "Products"
    ProductKey: int = Field(primary_key=True)
    ProductName: str
    Brand: Optional[str] = None
    UnitCost: Optional[float] = None
    UnitPrice: Optional[float] = None
    CategoryKey: Optional[int] = None
    SubCategoryKey: Optional[int] = None

class Sale(SQLModel, table=True):
    __tablename__ = "Sales"
    OrderNumber: int = Field(primary_key=True)
    LineItem: int = Field(primary_key=True)
    OrderDate: Optional[date] = None
    DeliveryDate: Optional[date] = None
    CustomerKey: Optional[int] = None
    StoreKey: Optional[int] = None
    ProductKey: Optional[int] = None
    Quantity: Optional[int] = None
    CurrencyCode: Optional[str] = None

class Store(SQLModel, table=True):
    __tablename__ = "Stores"
    StoreKey: int = Field(primary_key=True)
    Country: str
    State: Optional[str] = None
    SquareMeters: Optional[int] = None
    OpenDate: Optional[date] = None

class ExchangeRate(SQLModel, table=True):
    __tablename__ = "ExchangeRates"
    Date: date = Field(primary_key=True)
    Currency: str = Field(primary_key=True)
    Exchange: float