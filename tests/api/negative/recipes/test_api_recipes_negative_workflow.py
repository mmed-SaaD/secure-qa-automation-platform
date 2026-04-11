import requests, pytest

@pytest.mark.api
@pytest.mark.negative
def test_api_invalid_endpoint(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/invalidEndpoint")
    assert response.status_code == 404, \
        f"This endpoint is supposed to be invalid, expected 404 got {response.status_code} instead"

@pytest.mark.api
@pytest.mark.negative
@pytest.mark.xfail(reason="An empty body must raise an error instead of returning status code 200 for recipe creation")
def test_api_add_recipe_empty_body(API_BASE_URL):
    payload = {
        "prepTimeMinutes": "thirty",
        "servings": "six"
    }
    response = requests.post(f"{API_BASE_URL}/recipes/add", json=payload)
    assert response.status_code == 400, \
        f"Empty body, status code expected is 400, got {response.status_code} instead"

@pytest.mark.api
@pytest.mark.negative
@pytest.mark.xfail(reason="Target does not return 405 for invalid methods")
def test_api_invalid_method(API_BASE_URL):
    response = requests.delete(f"{API_BASE_URL}/recipes")
    assert response.status_code == 405

@pytest.mark.api
@pytest.mark.negative
@pytest.mark.xfail(reason="Target does not handle missing required fields, returns 200 instead of 400")
def test_api_add_recipe_with_missing_required_fields(API_BASE_URL):
    payload = {
        "name": "Moroccan Lamb Tagine",
        "ingredients": ["Lamb shoulder, cubed", "Onions, chopped", "Tomatoes, diced", "Preserved lemons", "Green olives", "Ras el hanout", "Saffron", "Fresh cilantro", "Olive oil"],
        "instructions": [
            "Season lamb with ras el hanout and saffron.",
            "In a tagine, heat olive oil and brown the lamb on all sides.",
            "Add chopped onions and cook until softened.",
            "Add diced tomatoes, preserved lemons, and olives.",
            "Cover and cook on low heat for 2 hours until lamb is tender.",
            "Garnish with fresh cilantro before serving."
        ],
        "prepTimeMinutes": 20,
        "cookTimeMinutes": 120,
        "userId": 7,
        "cuisine": "Moroccan",
        "tags": ["Tagine", "Moroccan", "Lamb"],
        "mealType": ["Dinner"]
    }
    response = requests.post(f"{API_BASE_URL}/recipes/add", json=payload)
    assert response.status_code == 400, \
        f"Missing required fields, expected 400 got {response.status_code} instead"