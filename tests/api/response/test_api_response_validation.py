import requests, pytest
from core.logger.get_logger import get_logger 
from src.api.recipe import Recipe

REQUIRED_HEADERS = ['Content-Type']
LOGGER = get_logger(__name__)

@pytest.mark.api
@pytest.mark.smoke
def test_api_response_status_headers(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/recipes")
    assert response.status_code == 200, f"Something went wrong, response returned status code {response.status_code}"
    for header in REQUIRED_HEADERS:
        assert header in response.headers.keys()
    assert 'application/json' in response.headers["Content-Type"] , f"Expected Content-Type to be application/json, got {response.headers["Content-Type"]} instead"

@pytest.mark.api
@pytest.mark.smoke
def test_api_body_parseable(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/recipes")
    assert response.status_code == 200, f"Something went wrong, response returned status code {response.status_code}"
    try:
        body = response.json()
        assert isinstance(body, dict)
    except Exception:
        pytest.fail("Body is not parseable")

@pytest.mark.api
@pytest.mark.smoke
def test_api_check_response_field_type(API_BASE_URL):
    response = response = requests.get(f"{API_BASE_URL}/recipes/11")
    assert response.status_code == 200, f"Something went wrong, response returned status code {response.status_code}"
    recipe = Recipe(**response.json())
    recipe.assert_fields_type_is_correct()

@pytest.mark.api
@pytest.mark.smoke
def test_api_check_non_nullability(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/recipes/11")
    assert response.status_code == 200, f"Something went wrong, response returned status code {response.status_code}"
    recipe = Recipe(**response.json())
    recipe.assert_non_nullability()

@pytest.mark.api
@pytest.mark.smoke
def test_api_check_str_not_empty(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/recipes/11")
    assert response.status_code == 200, f"Something went wrong, response returned status code {response.status_code}"
    recipe = Recipe(**response.json())
    recipe.assert_string_not_empty()