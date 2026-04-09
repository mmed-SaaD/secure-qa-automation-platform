import requests, pytest

@pytest.mark.api
@pytest.mark.smoke
def test_api_verify_limit_parameter(API_BASE_URL):
    params = {
        "limit" : 12,
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 200
    body = response.json()
    assert body["limit"] == params["limit"]
    assert len(body["products"]) == params["limit"]

@pytest.mark.api
@pytest.mark.smoke
def test_api_verify_skip_parameter(API_BASE_URL):
    params = {
        "skip" : 42,
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 200
    body = response.json()
    assert body["skip"] == params["skip"]
    for index, product in enumerate(body["products"]):      # => enumerate gives both the index and the item
        assert product["id"] == (params["skip"] + 1) + index

@pytest.mark.api
@pytest.mark.smoke
def test_api_verify_skip_limit_parameters(API_BASE_URL):
    params = {
        "limit" : 12,
        "skip" : 42,
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 200
    body = response.json()
    assert body["limit"] == params["limit"]
    assert body["skip"] == params["skip"]
    assert len(body["products"]) == params["limit"]
    for index, product in enumerate(body["products"]):      # => enumerate gives both the index and the item
        assert product["id"] == (params["skip"] + 1) + index

@pytest.mark.api
@pytest.mark.smoke
def test_api_zero_limit_parameter(API_BASE_URL):
    params = {
        "limit" : 0,
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 200
    body = response.json()
    assert len(body["products"]) > 0
    assert body["limit"] == body["total"]

@pytest.mark.api
@pytest.mark.smoke
def test_api_zero_skip_parameter(API_BASE_URL):
    params = {
        "skip" : 0,
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 200
    body = response.json()
    assert body["skip"] == params["skip"]
    for index, product in enumerate(body["products"]):    
        assert product["id"] == (params["skip"] + 1) + index

@pytest.mark.api
@pytest.mark.smoke
def test_api_boundary_limit_parameter(API_BASE_URL):
    total = requests.get(f"{API_BASE_URL}/products").json()["total"]
    params = {
        "limit" : total,
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 200
    body = response.json()
    assert len(body["products"]) == params["limit"]
    assert body["limit"] == body["total"]

@pytest.mark.api
@pytest.mark.smoke
def test_api_boundary_skip_parameter(API_BASE_URL):
    total = requests.get(f"{API_BASE_URL}/products").json()["total"]
    params = {
        "skip" : total,
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 200
    body = response.json()
    assert body["skip"] == params["skip"]
    assert len(body["products"]) == 0
    assert body["total"] > 0

@pytest.mark.api
@pytest.mark.smoke
def test_api_high_limit_parameter(API_BASE_URL):
    total = requests.get(f"{API_BASE_URL}/products").json()["total"]
    params = {
        "limit" : 9999,
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 200
    body = response.json()
    assert len(body["products"]) == total
    assert len(body["products"]) < params["limit"]
    assert body["limit"] == body["total"]

@pytest.mark.api
@pytest.mark.smoke
def test_api_high_skip_parameter(API_BASE_URL):
    total = requests.get(f"{API_BASE_URL}/products").json()["total"]
    params = {
        "skip" : 9999,
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 200
    body = response.json()
    assert total > 0
    assert body["skip"] == params["skip"]
    assert len(body["products"]) == 0
    assert body["total"] == total 

@pytest.mark.api
@pytest.mark.negative
def test_api_str_limit_parameter(API_BASE_URL):
    params = {
        "limit" : "string value instead of int",
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 400
    body = response.json()
    assert body["message"] == "Invalid 'limit' - must be a number"

@pytest.mark.api
@pytest.mark.negative
def test_api_str_skip_parameter(API_BASE_URL):
    params = {
        "skip" : "string value instead of int",
    }
    response = requests.get(f"{API_BASE_URL}/products", params = params)
    assert response.status_code == 400
    body = response.json()
    assert body["message"] == "Invalid 'skip' - must be a number"

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