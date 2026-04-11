import requests, pytest

@pytest.mark.api
@pytest.mark.negative
def test_api_malformed_auth_token(API_BASE_URL, api_login_token_verification, USERNAME_API, PASSWORD_API):
    headers = {
        'Content-Type': 'json/application',
        'Authorization': 'Bearer / Some random token value'
    }
    response = requests.get(f"{API_BASE_URL}/auth/me", headers=headers)
    assert response.status_code == 401, \
        f"Token is invalid, status code expected is 401, got {response.status_code} instead"

@pytest.mark.api
@pytest.mark.negative
def test_api_empty_auth_header(API_BASE_URL):
    headers = {
        "Authorization": ""
    }
    response = requests.get(f"{API_BASE_URL}/auth/recipes", headers=headers)
    assert response.status_code == 401, \
        f"Empty headers, status code expected is 401, got {response.status_code} instead"