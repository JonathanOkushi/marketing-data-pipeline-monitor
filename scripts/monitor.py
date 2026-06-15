import sqlite3
import pandas as pd
from pathlib import Path

from alerts import send_alerts

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "database"
DB_PATH = DB_DIR / "ads.db"

conn = sqlite3.connect(DB_PATH)

query = """
SELECT
    date,
    platform,
    spend,
    campaign,
    clicks,
    impressions,
    ctr,
    cpc,
    cpm
FROM
    transformed_ads_data
ORDER BY platform, campaign, date
"""

df = pd.read_sql_query(query, conn)

alerts = []

if df.empty:
    alerts.append("ALERT: No transformed ad data found.")

zero_activity = df[
    (df["spend"] == 0) |
    (df["clicks"] == 0) |
    (df["impressions"] == 0)
]

if not zero_activity.empty:
    alerts.append("ALERT: One or more compaigns have zero activity")

df["previous_day_spend"] = df.groupby(["platform", "campaign"])["spend"].shift(1)
df["spend_drop_percent"] = (
    ((df["previous_day_spend"] - df["spend"]) / df["previous_day_spend"]) * 100
)

large_drops = df[df["spend_drop_percent"] >= 81.8]
if not large_drops.empty:
    for _, row in large_drops.iterrows():
        alerts.append(
            f"ALERT: Campaign '{row['platform']}' - {row['campaign']} spend dropped "
            f"{row['spend_drop_percent']:.2f}% on {row['date']}"
        )

if alerts:
    print("Monitoring completed. Issues found:")
    for alert in alerts:
        print(alert)
        
    send_alerts(alerts)
else:
    print("Monitoring completed. No issues found.")
    
conn.close()
