import requests, pytest

@pytest.mark.api
@pytest.mark.smoke
def test_api_products_collection(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/products")
    assert response.status_code == 200
    body = response.json()
    assert len(body["products"]) > 0

    metadata_keys = ["products", "total", "skip", "limit"]
    for metadata_key in metadata_keys:
         assert metadata_key in body
    
    required_fields = ["id", "title", "price", "category"]
    for required_field in required_fields:
        for index in range (0 , len(body["products"])):
             assert required_field in body["products"][index]

    expected_types = {
        "id" : int,
        "title" : str,
        "price" : (int, float),
        "stock" : int,
        "rating" : float,
        "category" : str,
    }

    for field, expected_type in expected_types.items():
        for product in body["products"]:
            assert isinstance(product[field], expected_type), \
            f"Expected field [{field}] to be {expected_type}, got {type(product[field])} instead"

    ids = [product["id"] for product in body["products"]]
    assert len(ids) == len(set(ids)) , "IDs are not unique !"

    assert body["total"] > 0 , "No entries detected in the DB !"
    assert body["limit"] == len(body["products"]), "There is a missmatch between the limit and products returned"
    assert body["skip"] == 0
    assert body["skip"] + body["limit"] <= body["total"]

