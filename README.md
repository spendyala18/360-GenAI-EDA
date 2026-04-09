# 360-GenAI-EDA

A mini Applied Analytics project demonstrating ETL (Extract, Transform, Load) and secure querying.

## Setup Folder Structure
Run these commands to organize your files as intended:
```bash
mkdir -p data/raw data/db src tests
mv customers_raw.csv data/raw/
mv etl_load_sqlite.py src/
mv kpi_city.py src/
mv test_kpi_city.py tests/
```

## Run Commands

1. **Install Dependencies:**
   `pip install -r requirements.txt`

2. **Run ETL (Load CSV to SQLite):**
   `python src/etl_load_sqlite.py`

3. **Run KPI Script:**
   `python src/kpi_city.py`

4. **Run Tests:**
   `pytest`

## Verification

To verify the database exists and contains data:

- **Check file existence:**
  `ls data/db/` (PowerShell) or `ls -l data/db/` (Bash)
- **Verify tables via Python:**
  `python -c "import sqlite3; c=sqlite3.connect('data/db/analytics.db'); print(c.execute('SELECT name FROM sqlite_master;').fetchall())"`