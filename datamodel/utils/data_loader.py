import pandas as pd
import os

def load_dataframes(data_folder):
    """
    Loads CSV files into DataFrames and cleans column names.
    """
    file_paths = {
        "Customers": os.path.join(data_folder, "Customers.csv"),
        "ExchangeRates": os.path.join(data_folder, "Exchange_Rates.csv"),
        "Products": os.path.join(data_folder, "Products.csv"),
        "Sales": os.path.join(data_folder, "Sales.csv"),
        "Stores": os.path.join(data_folder, "Stores.csv")
    }

    dataframes = {}
    for name, path in file_paths.items():
        try:
            df = pd.read_csv(path, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(path, encoding="ISO-8859-1")
        # Remove spaces from column names
        df.columns = [col.replace(" ", "") for col in df.columns]
        dataframes[name] = df

    return dataframes