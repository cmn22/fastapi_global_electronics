import sqlite3

# Create a SQLite database and establish a connection
database_name = "Global_Electronics_Retailer.db"
conn = sqlite3.connect(database_name)
cursor = conn.cursor()

# SQL DDL Statements to create tables based on the provided database structure
sql_statements = [
    # Create Customers table
    """
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerKey INTEGER PRIMARY KEY,
        Gender TEXT,
        Name TEXT,
        City TEXT,
        StateCode TEXT,
        State TEXT,
        ZipCode TEXT,
        Country TEXT,
        Continent TEXT,
        Birthday DATE
    );
    """,

    # Create Products table
    """
    CREATE TABLE IF NOT EXISTS Products (
        ProductKey INTEGER PRIMARY KEY,
        ProductName TEXT,
        Brand TEXT,
        UnitCost FLOAT,
        UnitPrice FLOAT,
        CategoryKey INTEGER,
        SubCategoryKey INTEGER,
        FOREIGN KEY (CategoryKey) REFERENCES Category(CategoryKey),
        FOREIGN KEY (SubCategoryKey) REFERENCES SubCategory(SubCategoryKey)
    );
    """,

    # Create Sales table
    """
    CREATE TABLE IF NOT EXISTS Sales (
        OrderNumber INTEGER,
        LineItem INTEGER,
        OrderDate DATE,
        DeliveryDate DATE,
        CustomerKey INTEGER,
        StoreKey INTEGER,
        ProductKey INTEGER,
        Quantity INTEGER,
        CurrencyCode TEXT,
        PRIMARY KEY (OrderNumber, LineItem),
        FOREIGN KEY (CustomerKey) REFERENCES Customers(CustomerKey),
        FOREIGN KEY (StoreKey) REFERENCES Stores(StoreKey),
        FOREIGN KEY (ProductKey) REFERENCES Products(ProductKey)
    );
    """,

    # Create Stores table
    """
    CREATE TABLE IF NOT EXISTS Stores (
        StoreKey INTEGER PRIMARY KEY,
        Country TEXT,
        State TEXT,
        SquareMeters INTEGER,
        OpenDate DATE
    );
    """,

    # Create ExchangeRates table
    """
    CREATE TABLE IF NOT EXISTS ExchangeRates (
        Date DATE,
        Currency TEXT,
        Exchange FLOAT,
        PRIMARY KEY (Date, Currency)
    );
    """,

    # Create Category table
    """
    CREATE TABLE IF NOT EXISTS Category (
        CategoryKey INTEGER PRIMARY KEY,
        CategoryName TEXT
    );
    """,

    # Create SubCategory table
    """
    CREATE TABLE IF NOT EXISTS SubCategory (
        SubCategoryKey INTEGER PRIMARY KEY,
        SubCategoryName TEXT,
        CategoryKey INTEGER,
        FOREIGN KEY (CategoryKey) REFERENCES Category(CategoryKey)
    );
    """
]

# Execute the SQL statements to create the tables
for statement in sql_statements:
    cursor.execute(statement)

# Commit the changes and close the connection
conn.commit()
conn.close()

# Confirmation
print(f"SQLite database '{database_name}' and all tables have been created successfully.")