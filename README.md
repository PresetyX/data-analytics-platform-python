# Data Analytics Platform

Educational analytics platform built with Python, Flask, Pandas, NumPy, and scikit-learn.

## Features

- CSV ingestion and validation.
- Data cleaning and normalization.
- Sales KPIs and time-series summaries.
- Product and regional rankings.
- Baseline sales forecasting with linear regression.
- Flask REST API.
- Lightweight browser dashboard.
- Unit tests for ETL, metrics, forecasting, and API behavior.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -e ".[dev]"
python -m analytics_platform
```

Open `http://localhost:5000`.

## API

- `GET /health`
- `GET /api/summary`
- `GET /api/sales?region=Southeast`
- `GET /api/forecast?days=7`

## Example

```bash
curl http://localhost:5000/api/summary
curl "http://localhost:5000/api/forecast?days=7"
```

## Architecture

- `etl.py`: loading, validation, cleaning, and transformation.
- `metrics.py`: KPIs and grouped analytics.
- `forecast.py`: baseline forecast model.
- `app.py`: Flask application and API routes.
- `templates/`: dashboard presentation.

This is an educational project. Forecasts are illustrative and must not be used as business or financial advice.
