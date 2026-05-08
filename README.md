# Marketing Data Pipeline Monitoring System

## Overview

This project simulates a real-world analytics engineering workflow by building an automated ELT (Extract, Load, Transform) pipeline for marketing campaign data. The system ingests multi-platform advertising data, transforms raw metrics into analytics-ready reporting tables, detects silent pipeline failures, sends automated email alerts, and visualizes campaign performance in an interactive Power BI dashboard.

---

# Live Dashboard

👉 **Power BI Dashboard:**  
https://app.powerbi.com/view?r=eyJrIjoiNTA3ODViZjYtNWY4Ny00ZmUxLTlkZDQtZWUwNzczMDBkMGE3IiwidCI6ImE4MjE2YzFlLTRkNjMtNDM1Mi04YzNiLTUwZmExZjE0NzViMSIsImMiOjZ9

---

# Project Architecture

```text
CSV Ad Data
    ↓
ingest.py
    ↓
SQLite Database
    ↓
transform.py
    ↓
transformed_ads_data
    ↓
monitor.py
    ↓
Email Alerts
    ↓
Power BI Dashboard
```

---

# Key Features

- Automated ELT pipeline using Python and SQL
- Multi-platform ad data ingestion (Meta, Google, TikTok, LinkedIn)
- SQL-based KPI calculations:
  - CTR
  - CPC
  - CPM
- Automated anomaly detection:
  - zero-activity campaigns
  - missing data
  - 81.8% day-over-day spend drop detection
- Automated email alerting
- Interactive Power BI dashboard for campaign monitoring and trend analysis

---

# Technologies Used

- Python
- SQL
- SQLite
- pandas
- schedule
- smtplib
- Power BI

---

# How to Run

Install dependencies:

```bash
pip install pandas python-dotenv schedule
```

Run the pipeline:

```bash
python scripts/run_pipeline.py
```

---

