import re
import pytest

from app.app import app


@pytest.fixture
def client():
    """Flask test client fixture."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Test for successful home page response."""
    response = client.get("/")
    assert response.status_code == 200


def test_weather_api(client, requests_mock):
    """Test the weather API response. Note: Does not test the actual API or API key."""
    url = re.compile(
        r"http://api.openweathermap.org/data/2.5/weather\?q=Phoenix&appid=.+&units=imperial"
    )
    requests_mock.get(
        url,
        json={
            "main": {"temp": 115, "humidity": 17},
            "weather": [{"icon": "01d", "main": "clear", "description": "clear sky"}],
        },
    )
    response = client.post("/", data={"city": "Phoenix"})
    data = response.get_json()

    assert response.status_code == 200
    assert data["weather"]["temperature"] == 115
    assert data["weather"]["humidity"] == 17
    assert data["weather"]["icon"] == "01d"
    assert data["weather"]["type"] == "Clear"
    assert data["weather"]["description"] == "Clear Sky"
