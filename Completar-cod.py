import pandas as pd
import sqlite3

DB = 'candidates.db'
TABLE_NAME = 'candidate'

def almacenar_pandas_to_sql(df: pd.DataFrame, database_name: str, table_name: str) -> None:
    """Procesamiento datos candidatos para almacenarlos sobre db """

    # Rename columns
    column_rename = {c: c.replace(' ', '') for c in df.columns}
    df.rename(column_rename, axis='columns', inplace=True)

    # Connect to the database
    conn = sqlite3.connect(database_name)

    # Store the DataFrame in the database
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()

    # Print the number of records stored
    cantidad_registros = df.shape[0]
    print(f'Se almacenaron {cantidad_registros} registros en la tabla {table_name} de la base de datos {database_name}')

# Read the CSV file
path = './src/candidates.csv'
df = pd.read_csv(path, sep=';')

# Call the function to store the data in the database
almacenar_pandas_to_sql(df, DB, TABLE_NAME)
