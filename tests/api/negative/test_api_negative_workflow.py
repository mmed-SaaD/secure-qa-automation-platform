import requests, pytest

@pytest.mark.api
@pytest.mark.negative
def test_api_invalid_endpoint(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/invalidEndpoint")
    assert response.status_code == 404, \
    f"This endpoint is supposed to be invalid, status code expected 404 got {response.status_code} instead"

@pytest.mark.api
@pytest.mark.negative
def test_api_invalid_product_id(API_BASE_URL, productID : int = 9999):
    response = requests.get(f"{API_BASE_URL}/products/{productID}")
    assert response.status_code == 404, \
    f"Product ID is invalid, status code expected is 404, got {response.status_code} instead"

@pytest.mark.api
@pytest.mark.negative
def test_api_malformed_auth_token(API_BASE_URL, api_login_token_verification, USERNAME_API, PASSWORD_API):
    token = api_login_token_verification
    headers = {
        'Content-Type' : 'json/application',
        'Authorization' : 'Bearer / Some random token value'
    }
    response = requests.get(f"{API_BASE_URL}/auth/me", headers = headers)
    assert response.status_code == 401, \
    f"Token is invalid, status code expected is 401, got {response.status_code} instead"

@pytest.mark.api
@pytest.mark.negative
def test_api_empty_headers_recipe_fetching(API_BASE_URL):
    headers = {
        "Authorization" : ""
    }
    response = requests.get(f"{API_BASE_URL}/auth/recipes", headers = headers)
    assert response.status_code == 401 , f"Empty headers, status code expected is 401, got {response.status_code} instead"

@pytest.mark.api
@pytest.mark.negative
@pytest.mark.xfail(reason="An empty body must raise an error instead of returning status code 200 for recipe creation")
def test_api_add_recipe_empty_body(API_BASE_URL):
    payload = {
        "prepTimeMinutes": "thirty",
        "servings": "six"
    }
    response = requests.post(f"{API_BASE_URL}/recipe/add", json=payload)
    assert response.status_code == 400, f"Empty body, status code expected is 401, got {response.status_code} instead"

@pytest.mark.api
@pytest.mark.negative
@pytest.mark.fail(reason="Target does not return 405 for invalid methods")
def test_api_invalid_method(API_BASE_URL):
    response = requests.delete(f"{API_BASE_URL}/recipes")
    assert response.status_code == 405


