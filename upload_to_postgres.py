import pandas as pd
import psycopg2
import os

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="stock_analysis",
    user="postgres",
    password="252806"   
)
cursor = conn.cursor()

DATA_PATH = "data/cleaned_csv"

for file in os.listdir(DATA_PATH):
    if file.endswith(".csv"):
        symbol = file.replace(".csv", "")
        df = pd.read_csv(os.path.join(DATA_PATH, file))

        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO stocks (date, symbol, open, high, low, close, volume)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                row["date"], symbol,
                row["open"], row["high"], row["low"],
                row["close"], row["volume"]
            ))

conn.commit()
cursor.close()
conn.close()

print("✅ Data uploaded to PostgreSQL successfully")