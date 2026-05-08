import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "ads.db"
EXPORT_PATH = BASE_DIR / "data" / "powerbi_ads_dashboard.csv"

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql_query("SELECT * FROM transformed_ads_data", conn)
df.to_csv(EXPORT_PATH, index=False)

conn.close()

print(f"Data exported successfully to {str(EXPORT_PATH)}")