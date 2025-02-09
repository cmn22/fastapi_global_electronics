# Global Electronics Retailer API
This project is a FastAPI-based web service for managing various components of an electronics retail business. It includes endpoints for Customers, Products, Sales, Stores, Exchange Rates, Categories, and Subcategories. The system utilizes an SQLite database with SQLModel as the ORM for structured data handling.

## ✨ Features
- CRUD operations for Customers, Products, Sales, Stores and Exchange Rates
- Pagination for optimized data retrieval
- Date handling for fields like birthdays, order dates, and exchange rate timestamps
- API documentation available via Swagger UI (/docs) and ReDoc (/redoc)
- Uses SQLModel (a combination of Pydantic and SQLAlchemy) for data modeling
- Fast and lightweight API with dependency injection for database sessions

## ⚙ Installation & Setup

1. Clone the Repository
```
git clone https://github.com/yourusername/global-electronics-retailer.git
cd global-electronics-retailer
```

2. Create a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

3. Install Dependencies
```
pip install -r requirements.txt
```

## 💽 Database Setup
The database is SQLite-based and will be automatically created upon running the setup scripts.

1. Create the Database Schema
```
python datamodel/create_db.py
```
This will create an Global_Electronics_Retailer.db file in the project root.

2. Populate the Database with Initial Data
```
python datamodel/populate_db.py
```
This script loads sample data from CSV files and populates the database.

3. Verify the Database

To check the database structure:
```
sqlite3 Global_Electronics_Retailer.db
```
Inside SQLite CLI, list tables:
```
.tables
```

## 🚀 Running the FastAPI Server

1. Start the API

Run the following command to start the FastAPI server:
```
uvicorn api.main:app --reload
```

2. Access API Documentation

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc


## 📝 API Endpoints Overview

### Customers
| **Method** | **Endpoint**   | **Description**                    |
|------------|----------------|------------------------------------|
| GET        | /              | Get all customers with pagination. |
| GET        | /{customer_id} | Get a single customer by ID.       |
| POST       | /              | Create a new customer.             |
| PUT        | /{customer_id} | Update an existing customer.       |
| DELETE     | /{customer_id} | Delete a customer.                 |

### Products
| **Method** | **Endpoint**  | **Description**                   |
|------------|---------------|-----------------------------------|
| GET        | /             | Get all products with pagination. |
| GET        | /{product_id} | Get a single product by ID.       |
| POST       | /             | Create a new product.             |
| PUT        | /{product_id} | Update an existing product.       |
| DELETE     | /{product_id} | Delete a product.                 |

### Sales
| **Method** | **Endpoint**                | **Description**                       |
|------------|-----------------------------|---------------------------------------|
| GET        | /                           | Get all sales with pagination.        |
| GET        | /{order_number}/{line_item} | Get a sale by OrderNumber & LineItem. |
| POST       | /                           | Create a new sale.                    |
| DELETE     | /{order_number}/{line_item} | Delete a sale.                        |

### Stores
| **Method** | **Endpoint**       | **Description**                 |
|------------|--------------------|---------------------------------|
| GET        | /                  | Get all stores with pagination. |
| GET        | /{store_id}        | Get a store by ID.              |
| POST       | /                  | Create a new store.             |
| DELETE     | /{store_id}        | Delete a store.                 |

### Exchange Rates
| **Method** | **Endpoint**       | **Description**                         |
|------------|--------------------|-----------------------------------------|
| GET        | /                  | Get all exchange rates with pagination. |
| GET        | /{date}/{currency} | Get exchange rate by date and currency. |
| POST       | /                  | Create a new exchange rate entry.       |
| PUT        | /{date}/{currency} | Update an exchange rate entry.          |
| DELETE     | /{date}/{currency} | Delete an exchange rate entry.          |


## 🔮 Running API Tests

We have Jupyter notebooks to test the API.

1. Start the API Server

Ensure the FastAPI server is running before executing test scripts.

2. Run Jupyter Notebooks
```
jupyter notebook
```
Then open and execute:
```
tests/test_customers_api.ipynb

tests/test_products_api.ipynb

tests/test_sales_api.ipynb

tests/test_stores_api.ipynb

tests/test_exchange_rates_api.ipynb
```

## ⚒️ Development Notes
- Ensure that the database is set up before running the API.
- Always activate the virtual environment before running scripts.
- Use uvicorn for local API testing.
- Run populate_db.py whenever fresh test data is needed.

## 📚 License
This project is open-source and available under the MIT License.

