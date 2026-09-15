from analytics_platform.app import create_app


def test_health_endpoint():
    client = create_app("data/sample_sales.csv").test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_forecast_validation():
    client = create_app("data/sample_sales.csv").test_client()
    response = client.get("/api/forecast?days=0")
    assert response.status_code == 400
