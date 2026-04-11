import requests, pytest
from src.api.product import Product
from src.api.recipe import Recipe
from src.api.cart import Cart
from src.api.user_informations.user import User

@pytest.mark.api
@pytest.mark.smoke
def test_api_response_products_collection_schema(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/products")
    assert response.status_code == 200, f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    assert "products" in body , "Missing products !"
    assert len(body["products"]) > 0 , "No products retrieved !"
    for product in body["products"]:
        p = Product(**product)
        p.assert_shape_stability()
        p.assert_fields_type()

@pytest.mark.api
@pytest.mark.smoke
def test_api_response_single_recipe_schema(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/recipes/7")
    assert response.status_code == 200 , f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    recipe = Recipe(**body)
    recipe.assert_required_fields_exist()
    recipe.assert_fields_type_is_correct()

@pytest.mark.api
@pytest.mark.smoke
def test_api_response_cart_schema(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/carts")
    assert response.status_code == 200, f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    assert "carts" in body, f"carts is missing !"
    assert len(body["carts"]) > 0, f"No carts were retrieved !"
    for cart in body["carts"]:
        c = Cart(**cart)
        c.assert_expected_cart_keys_exist_with_correct_types()
    
@pytest.mark.api
@pytest.mark.smoke
def test_api_response_error_schema(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/carts/invalid")
    assert response.status_code != 200, f"This request is not supposed to be valid, but still got status code {response.status_code}"
    body = response.json()
    assert "message" in body, "Error message is missing !"
    assert len(body["message"]) > 0

@pytest.mark.api
@pytest.mark.smoke
def test_api_response_auth_response_schema(API_BASE_URL, api_login_token_verification, USERNAME_API, PASSWORD_API):
    token = api_login_token_verification
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : f'Bearer {token}'
    }
    response = requests.get(f"{API_BASE_URL}/auth/me" , headers = headers)
    assert response.status_code == 200, f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    user = User(**body)
    user.assert_expected_keys_exist_and_types_are_valid()
    