import pandas as pd
from sklearn.linear_model import LinearRegression


def forecast_revenue(frame: pd.DataFrame, days: int = 7) -> list[dict]:
    if days < 1 or days > 90:
        raise ValueError("days must be between 1 and 90")
    daily = frame.groupby("date", as_index=False)["revenue"].sum().sort_values("date")
    if len(daily) < 2:
        return []
    x = (daily["date"] - daily["date"].min()).dt.days.to_numpy().reshape(-1, 1)
    y = daily["revenue"].to_numpy()
    model = LinearRegression().fit(x, y)
    last_date = daily["date"].max()
    future_x = (last_date - daily["date"].min()).days + 1
    dates = pd.date_range(last_date + pd.Timedelta(days=1), periods=days)
    predictions = model.predict([[future_x + i] for i in range(days)])
    return [{"date": date.strftime("%Y-%m-%d"), "predicted_revenue": round(max(0.0, float(value)), 2)} for date, value in zip(dates, predictions)]
