import pandas as pd
from analytics_platform.etl import load_sales
from analytics_platform.forecast import forecast_revenue
from analytics_platform.metrics import summary


def test_load_sales_calculates_revenue(tmp_path):
    file = tmp_path / "sales.csv"
    file.write_text("date,product,region,units,unit_price\n2026-01-01,Mouse,South,2,10\n")
    frame = load_sales(file)
    assert frame.iloc[0]["revenue"] == 20


def test_summary():
    frame = pd.DataFrame({"date": pd.to_datetime(["2026-01-01"]), "product": ["Mouse"], "region": ["South"], "units": [2], "unit_price": [10], "revenue": [20]})
    result = summary(frame)
    assert result["total_revenue"] == 20
    assert result["top_product"] == "Mouse"


def test_forecast_returns_requested_days():
    frame = pd.DataFrame({"date": pd.to_datetime(["2026-01-01", "2026-01-02"]), "revenue": [10, 20]})
    result = forecast_revenue(frame, 3)
    assert len(result) == 3
