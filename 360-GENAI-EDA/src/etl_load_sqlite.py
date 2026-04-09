import pandas as pd
import sqlite3
import os

def run_etl():
    # Ensure directories exist
    os.makedirs('data/db', exist_ok=True)
    
    # Load data
    csv_path = 'data/raw/customers_raw.csv'
    if not os.path.exists(csv_path):
        # Fallback to root if the user hasn't created the data/raw folder yet
        csv_path = 'customers_raw.csv'
    
    print(f"Reading from: {csv_path}")
    df = pd.read_csv(csv_path)
    
    # Connect to SQLite and save
    conn = sqlite3.connect('data/db/analytics.db')
    df.to_sql('customers_raw', conn, if_exists='replace', index=False)
    conn.close()
    print("Success: Data loaded from CSV to data/db/analytics.db")

if __name__ == "__main__":
    run_etl()