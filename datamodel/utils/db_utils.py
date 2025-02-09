def get_table_columns(cursor, table_name):
    """
    Fetches column names of a table from the SQLite database.
    """
    cursor.execute(f"PRAGMA table_info({table_name});")
    return [info[1] for info in cursor.fetchall()]

def insert_data(cursor, table_name, dataframe):
    """
    Inserts data into a SQLite table from a DataFrame.
    """
    # Get the list of columns in the table
    table_columns = get_table_columns(cursor, table_name)

    # Filter DataFrame to include only columns that exist in the table
    dataframe = dataframe[[col for col in dataframe.columns if col in table_columns]]

    # Generate column and value placeholders
    columns = ", ".join([f'"{col}"' for col in dataframe.columns])
    placeholders = ", ".join(["?"] * len(dataframe.columns))
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    print(f"Inserting into {table_name} with query: {sql}")
    for _, row in dataframe.iterrows():
        cursor.execute(sql, tuple(row))