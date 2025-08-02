from sqlalchemy import create_engine
import pandas as pd
from urllib.parse import quote_plus

# Connection details
username = 'SA'
password = 'Sachin@1234'
server = 'localhost'
database = 'AdventureWorks2022'

# Encode driver name for URL
driver = quote_plus('ODBC Driver 17 for SQL Server')

# SQLAlchemy connection string
connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    f"?driver={driver}&TrustServerCertificate=yes"
)

# Create engine
engine = create_engine(connection_string)

# Query to fetch data
query = "SELECT TOP 10 * FROM Production.Product"

# Execute query and load result into DataFrame
df = pd.read_sql(query, engine)
print(df)
