import requests, pytest

@pytest.mark.api
@pytest.mark.negative
def test_api_str_limit_parameter(API_BASE_URL):
    params = {
        "limit" : "string value instead of int",
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 400
    body = response.json()
    assert "limit" in body["message"].lower()

@pytest.mark.api
@pytest.mark.negative
def test_api_str_skip_parameter(API_BASE_URL):
    params = {
        "skip" : "string value instead of int",
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 400
    body = response.json()
    assert "skip" in body["message"].lower()

@pytest.mark.api
@pytest.mark.negative
def test_api_negative_limit_parameter(API_BASE_URL):
    total = requests.get(f"{API_BASE_URL}/products").json()["total"]
    params = {
        "limit" : -156,
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    body = response.json()
    assert response.status_code == 200
    assert body["limit"] == total + int(params["limit"])
    assert len(body["products"]) == body["limit"]

@pytest.mark.api
@pytest.mark.negative
def test_api_negative_skip_parameter(API_BASE_URL):
    limit = requests.get(f"{API_BASE_URL}/products").json()["limit"]
    params = {
        "skip" : -174,
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 200
    body = response.json()
    assert len(body["products"]) == limit