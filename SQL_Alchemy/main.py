import pyodbc
from sqlalchemy import create_engine, text
import pandas as pd
from urllib.parse import quote_plus

# Config
server = 'localhost'
port = '1433'
database = 'master'
username = 'SA'
password = 'Sachin@1234'

# Step 1: pyodbc (works)
print("Connecting using pyodbc...")
try:
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(conn_str, timeout=5)
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    row = cursor.fetchone()
    print("SQL Server Version (pyodbc):", row[0])
except Exception as e:
    print("pyodbc connection failed:", e)

# Step 2: SQLAlchemy (fix with quote_plus)
print("\nConnecting using SQLAlchemy...")
try:
    params = quote_plus(
        f"DRIVER=ODBC Driver 17 for SQL Server;"
        f"SERVER={server},{port};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    sqlalchemy_conn_str = f"mssql+pyodbc:///?odbc_connect={params}"
    engine = create_engine(sqlalchemy_conn_str, fast_executemany=True)

    with engine.connect() as connection:
        result = connection.execute(text("SELECT GETDATE()"))
        for row in result:
            print("SQLAlchemy Result:", row)
except Exception as e:
    print("SQLAlchemy connection failed:", e)

# Step 3: Pandas
print("\nUsing pandas to query and display a table...")
try:
    df = pd.read_sql("SELECT TOP 5 name FROM sys.databases", engine)
    print(df)
except Exception as e:
    print("Pandas query failed:", e)
