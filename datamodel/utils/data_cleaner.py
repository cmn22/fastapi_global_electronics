def preprocess_products(products_df):
    """
    Cleans and preprocesses the Products DataFrame.
    """
    if "UnitCost" in products_df.columns:
        products_df["UnitCost"] = (
            products_df["UnitCost"].str.replace(r"[$,]", "", regex=True).astype(float)
        )
    if "UnitPrice" in products_df.columns:
        products_df["UnitPrice"] = (
            products_df["UnitPrice"].str.replace(r"[$,]", "", regex=True).astype(float)
        )
    return products_df

def extract_categories_subcategories(products_df, key_column, name_column):
    """
    Extracts unique categories or subcategories from the Products DataFrame.
    """
    return products_df[[key_column, name_column]].drop_duplicates().rename(
        columns={name_column: f"{name_column}Name"}
    )