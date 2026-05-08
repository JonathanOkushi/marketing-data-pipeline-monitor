import pandas as pd
import sqlite3
from pathlib import Path

#Define project folders
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_DIR = BASE_DIR / "database"
DB_PATH = DB_DIR / "ads.db"

DB_DIR.mkdir(exist_ok=True)


#Reading CSV Files
meta_df = pd.read_csv(DATA_DIR / "meta_ads.csv")
tiktok_df = pd.read_csv(DATA_DIR / "tiktok_ads.csv")

meta_df["platform"] = "Meta"
tiktok_df["platform"] = "TikTok"


#Combine DataFrames
ads_df = pd.concat([meta_df, tiktok_df], ignore_index=True)

#Connecting to database
conn = sqlite3.connect(DB_PATH)

#Ingesting data into database
ads_df.to_sql(
    "raw_ads_data",
    conn,
    if_exists="replace",
    index=False
)

#Closing Connnection
conn.close()

print("CSV files successfully loaded into database!")
print(f"Rows loaded: {len(ads_df)}")
print(f"Database created at: {DB_PATH}")