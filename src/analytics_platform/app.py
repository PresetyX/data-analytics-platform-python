import os
from pathlib import Path
from flask import Flask, jsonify, render_template, request
from .etl import load_sales
from .forecast import forecast_revenue
from .metrics import daily_sales, sales_by_product, sales_by_region, summary


def create_app(data_path: str | None = None) -> Flask:
    app = Flask(__name__)
    path = Path(data_path or os.getenv("DATA_PATH", "data/sample_sales.csv"))
    frame = load_sales(path)

    @app.get("/")
    def dashboard():
        return render_template("dashboard.html", data=summary(frame))

    @app.get("/health")
    def health():
        return jsonify({"status": "ok", "rows_loaded": len(frame)})

    @app.get("/api/summary")
    def api_summary():
        return jsonify(summary(frame))

    @app.get("/api/sales")
    def api_sales():
        current = frame
        region = request.args.get("region")
        if region:
            current = current[current["region"].str.casefold() == region.casefold()]
        return jsonify({"by_product": sales_by_product(current), "by_region": sales_by_region(current), "daily": daily_sales(current)})

    @app.get("/api/forecast")
    def api_forecast():
        days = request.args.get("days", default=7, type=int)
        try:
            return jsonify(forecast_revenue(frame, days))
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

    return app
