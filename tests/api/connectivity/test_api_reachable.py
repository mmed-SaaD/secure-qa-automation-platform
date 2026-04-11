import requests, pytest

@pytest.mark.smoke
@pytest.mark.api
def test_api_is_reachable(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/test")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 3
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.parametrize("endpoint",  [
    "/products",
    "/users",
    "/carts",
    "/comments",
    "/recipes",
    "/posts",
    "/todos",
    "/quotes",
])
def test_api_core_endpoints(API_BASE_URL, endpoint):
    response = requests.get(f"{API_BASE_URL}{endpoint}")
    assert response.status_code == 200

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.parametrize("endpoint, key_word" , [
    ("/products" , "products"),
    ("/carts" , "carts"),
    ("/comments", "comments"),
    ("/users", "users"),
    ("/recipes", "recipes"),
    ("/posts", "posts"),
    ("/todos", "todos"),
])
def test_api_endpoint_body_form(API_BASE_URL, endpoint, key_word):
    response = requests.get(f"{API_BASE_URL}{endpoint}")
    assert response.status_code == 200
    body = response.json()

    assert isinstance(body, dict)
    assert key_word in body
    assert isinstance(body[key_word], list)
    assert len(body[key_word]) > 0
