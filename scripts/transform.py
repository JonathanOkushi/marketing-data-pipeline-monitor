import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "database"
DB_PATH = DB_DIR / "ads.db"

conn = sqlite3.connect(DB_PATH)

query = """
SELECT
    date,
    platform,
    campaign,
    spend,
    clicks,
    impressions,
    ROUND(
        (clicks * 1.0 / impressions) * 100, 2
    ) AS ctr,
    ROUND(
        (spend * 1.0 / clicks), 2
    ) AS cpc, 
    ROUND(
        (spend * 1000.0 / impressions), 2
    ) AS cpm
FROM
    raw_ads_data
WHERE impressions > 0
"""

transformed_df = pd.read_sql_query(query, conn)
transformed_df.to_sql(
    "transformed_ads_data",
    conn,
    if_exists="replace",
    index=False
)

conn.close()
print("Data transformation complete!")
print(f"Transformed Rows: {len(transformed_df)}")
