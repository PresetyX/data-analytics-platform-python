import pandas as pd


def summary(frame: pd.DataFrame) -> dict:
    return {
        "rows": int(len(frame)),
        "total_revenue": round(float(frame["revenue"].sum()), 2),
        "total_units": int(frame["units"].sum()),
        "average_order_value": round(float(frame["revenue"].mean()), 2),
        "top_product": frame.groupby("product")["revenue"].sum().idxmax(),
        "top_region": frame.groupby("region")["revenue"].sum().idxmax(),
    }


def sales_by_product(frame: pd.DataFrame) -> list[dict]:
    grouped = frame.groupby("product", as_index=False).agg(revenue=("revenue", "sum"), units=("units", "sum"))
    return grouped.sort_values("revenue", ascending=False).round(2).to_dict("records")


def sales_by_region(frame: pd.DataFrame) -> list[dict]:
    grouped = frame.groupby("region", as_index=False).agg(revenue=("revenue", "sum"), units=("units", "sum"))
    return grouped.sort_values("revenue", ascending=False).round(2).to_dict("records")


def daily_sales(frame: pd.DataFrame) -> list[dict]:
    grouped = frame.groupby("date", as_index=False)["revenue"].sum()
    grouped["date"] = grouped["date"].dt.strftime("%Y-%m-%d")
    return grouped.round(2).to_dict("records")
