from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from api.endpoints import customers, products, sales, stores, exchange_rates

app = FastAPI(
    title="Global Electronics Retailer API",
    description="API for managing customers, products, sales, stores, and exchange rates.",
    version="1.0.0",
)

templates = Jinja2Templates(directory="templates")

app.include_router(customers.router)
app.include_router(products.router)
app.include_router(sales.router)
app.include_router(stores.router)
app.include_router(exchange_rates.router)

@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})