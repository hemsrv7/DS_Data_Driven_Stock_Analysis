import os
import yaml
import pandas as pd

RAW_YAML_DIR = os.path.join("data", "raw_yaml")
OUTPUT_DIR = os.path.join("data", "processed_csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

all_records = []

for file in os.listdir(RAW_YAML_DIR):
    if file.endswith(".yaml"):
        file_path = os.path.join(RAW_YAML_DIR, file)

        with open(file_path, "r") as f:
            data = yaml.safe_load(f)

            # ✅ data is a LIST → loop through it
            if isinstance(data, list):
                for record in data:
                    all_records.append(record)

df = pd.DataFrame(all_records)

output_file = os.path.join(OUTPUT_DIR, "stock_data.csv")
df.to_csv(output_file, index=False)

print("YAML to CSV conversion completed successfully")