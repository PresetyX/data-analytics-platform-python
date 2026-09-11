from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {"date", "product", "region", "units", "unit_price"}


def load_sales(path: str | Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    missing = REQUIRED_COLUMNS - set(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    frame["units"] = pd.to_numeric(frame["units"], errors="coerce")
    frame["unit_price"] = pd.to_numeric(frame["unit_price"], errors="coerce")
    frame = frame.dropna(subset=["date", "product", "region", "units", "unit_price"])
    frame = frame[(frame["units"] > 0) & (frame["unit_price"] >= 0)].copy()
    frame["revenue"] = frame["units"] * frame["unit_price"]
    return frame.sort_values("date").reset_index(drop=True)
