import sqlite3
from utils.data_loader import load_dataframes
from utils.data_cleaner import preprocess_products, extract_categories_subcategories
from utils.db_utils import insert_data

# SQLite database connection
db_path = "Global_Electronics_Retailer.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Load DataFrames from CSV files
data_folder = "datamodel/data"
dataframes = load_dataframes(data_folder)

# Preprocess Products DataFrame
products_df = preprocess_products(dataframes["Products"])

# Extract Categories and Subcategories
categories = extract_categories_subcategories(products_df, "CategoryKey", "Category")
subcategories = extract_categories_subcategories(products_df, "SubCategoryKey", "SubCategory")

# Populate tables in the database
insert_data(cursor, "Customers", dataframes["Customers"])
insert_data(cursor, "ExchangeRates", dataframes["ExchangeRates"])
insert_data(cursor, "Products", products_df)
insert_data(cursor, "Sales", dataframes["Sales"])
insert_data(cursor, "Stores", dataframes["Stores"])
insert_data(cursor, "Category", categories)
insert_data(cursor, "SubCategory", subcategories)

# Commit and close connection
conn.commit()
conn.close()

print("Database tables populated successfully.")