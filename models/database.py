import pyodbc
import pandas as pd
import dotenv
import os

dotenv.load_dotenv()

CONN_STR = os.getenv('CONN_STR')

def get_contacts():
    """fetch all contacts from the database"""
    conn = pyodbc.connect(CONN_STR)
    query = "SELECT * FROM contacts"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_goals():
    """fetch all goals from the database"""
    conn = pyodbc.connect(CONN_STR)
    query = "SELECT * FROM goals"
    df = pd.read_sql(query, conn)
    conn.close()
    return df