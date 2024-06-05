import pandas as pd
from sqlalchemy import create_engine

# Database connection string
db_connection_str = 'postgresql://postgres:password@localhost/ccdb'
db_connection = create_engine(db_connection_str)

# Load the Excel file
excel_file_path = 'D:/POWER BI/credit_card.xlsx'
df = pd.read_excel(excel_file_path)

# Insert data into PostgreSQL
df.to_sql('cc_detail', db_connection, if_exists='replace', index=False)
