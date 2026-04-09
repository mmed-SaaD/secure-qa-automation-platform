import pytest, requests


@pytest.mark.auth
@pytest.mark.api
@pytest.mark.smoke
def test_login_valid_credentials(API_BASE_URL, USERNAME_API, PASSWORD_API):
    payload = {
        "username" : USERNAME_API,
        "password" : PASSWORD_API
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(f"{API_BASE_URL}/auth/login",  payload)
    assert response.status_code == 200 , f"Something went wrong, response returned status code {response.status_code}"

    data = response.json()
    assert "accessToken" in data
    assert len(data["accessToken"]) > 0

@pytest.mark.auth
@pytest.mark.api
@pytest.mark.smoke
def test_valide_auth_protected_endpoint_access(API_BASE_URL, USERNAME_API, PASSWORD_API):
    payload = {
        "username" : USERNAME_API,
        "password" : PASSWORD_API
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(f"{API_BASE_URL}/auth/login",  payload)
    assert response.status_code == 200

    data = response.json()
    assert "accessToken" in data
    assert len(data["accessToken"]) > 0
    headers = {
        "Authorization" : f"Bearer {data["accessToken"]}"
    }
    response = requests.get(f"{API_BASE_URL}/auth/products", headers = headers)
    assert response.status_code == 200
    body = response.json()
    assert "products" in body
    assert len(body["products"]) > 0

@pytest.mark.unauthorized
@pytest.mark.api
def test_protected_endpoint_access_invalid_auth(API_BASE_URL):
    payload = {
        "username" : "invalid_username",
        "password" : "invalid_p@ss007"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(f"{API_BASE_URL}/auth/login", payload, headers)
    assert response.status_code == 400

    response = requests.get(f"{API_BASE_URL}/auth/products")
    assert response.status_code == 401

@pytest.mark.auth
@pytest.mark.api
def test_login_invalid_credentials(API_BASE_URL):
    payload = {
        "username" : "invalid_username",
        "password" : "invalid_p@ss007"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(f"{API_BASE_URL}/auth/login",  payload)

    assert response.status_code == 400

@pytest.mark.api
@pytest.mark.unauthorized
def test_unauthorized_products_listing(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/auth/products")
    data = response.json()
    assert "message" in data
    assert data["message"] == "Access Token is required"
    assert response.status_code == 401

