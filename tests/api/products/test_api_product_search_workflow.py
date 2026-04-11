import requests, pytest
from src.api.product import Product

SEARCH_KEYWORD = "sunglasses"
NON_EXISTING_KEYWORD = "exir"
CATEGORY = "smartphones"

@pytest.mark.api
@pytest.mark.smoke
def test_api_search_product_by_keyword(API_BASE_URL):
    params = {
        "q" : SEARCH_KEYWORD
    }
    response = requests.get(f"{API_BASE_URL}/products/search", params=params)
    assert response.status_code == 200, f"There has been an error, status_code = {response.status_code}"
    body = response.json()
    assert len(body["products"]) > 0 , f"No product matches the keyword {SEARCH_KEYWORD}"
    for product in body["products"]:
        product = Product.from_dict(product)
        product.assert_required_fields_exist()
        product.assert_fields_type()

@pytest.mark.api
@pytest.mark.smoke
def test_api_assert_matching_records(API_BASE_URL):
    params = {
        "q" : SEARCH_KEYWORD
    }
    response = requests.get(f"{API_BASE_URL}/products/search", params=params)
    body = response.json()
    assert len(body["products"]) > 0 , f"No product matches the keyword {SEARCH_KEYWORD}"
    for product in body["products"]:
        assert SEARCH_KEYWORD in product["title"].lower() or SEARCH_KEYWORD in product["description"].lower() , \
        f"{SEARCH_KEYWORD} cannot be found in the product's title nor description"

@pytest.mark.api
def test_api_non_existing_product(API_BASE_URL):
    params = {
        "q" : NON_EXISTING_KEYWORD
    }
    response = requests.get(f"{API_BASE_URL}/products/search", params=params)
    assert response.status_code == 200  # ← missing
    body = response.json()
    assert len(body["products"]) == 0 
    assert body["total"] == 0
    
@pytest.mark.api
@pytest.mark.smoke
def test_api_product_filtering_by_category(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/products/category/{CATEGORY}")
    body = response.json()
    assert len(body["products"]) > 0 , f"No products found for category {CATEGORY}"
    for product in body["products"]:
        assert CATEGORY in product["category"].lower()
