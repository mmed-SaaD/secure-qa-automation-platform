import requests, pytest
from src.api.product import Product

@pytest.mark.api
@pytest.mark.smoke
def test_api_product_details(API_BASE_URL):
    id = 14
    response = requests.get(f"{API_BASE_URL}/products/{id}")
    assert response.status_code == 200
    body = response.json()
    product = Product.from_dict(body)

    product.assert_product_id(int(id))
    
    product.assert_required_fields_exist()
    
    product.assert_fields_type()
    
    product.assert_price_is_positive()
    
    product.assert_title_is_not_empty()
    
    product.assert_category_is_not_empty()
    
    product.assert_shape_stability()
