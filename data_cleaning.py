import pandas as pd
import os

INPUT_PATH = "data/processed_csv"
OUTPUT_PATH = "data/cleaned_csv"

os.makedirs(OUTPUT_PATH, exist_ok=True)

for file in os.listdir(INPUT_PATH):
    if file.endswith(".csv"):
        file_path = os.path.join(INPUT_PATH, file)

        df = pd.read_csv(file_path)

        # Convert date column
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

        # Remove duplicates
        df.drop_duplicates(inplace=True)

        # Handle missing values
        df.fillna(method="ffill", inplace=True)

        # Sort by date
        df.sort_values("date", inplace=True)

        # Save cleaned file
        df.to_csv(os.path.join(OUTPUT_PATH, file), index=False)

print("✅ Data cleaning completed")