import pytest, requests
from src.api.recipe import Recipe

@pytest.mark.api
@pytest.mark.smoke
def test_api_add_recipe(API_BASE_URL):
    headers = {
        'Content-Type' : 'Application/json'
    }
    data = {
        "name":"Moroccan Harira Soup",
        "ingredients":["Lamb, diced","Chickpeas, cooked","Lentils","Tomatoes, chopped","Onions, finely chopped","Celery, chopped","Ginger, grated","Turmeric","Cinnamon","Cumin","Fresh cilantro, chopped","Fresh parsley, chopped","Lemon juice","Vermicelli noodles","Salt and pepper to taste"],
        "instructions":["In a large pot, brown diced lamb in oil.","Add chopped onions, celery, ginger, turmeric, cinnamon, and cumin. Stir well.","Add chopped tomatoes, chickpeas, and lentils. Cover with water and bring to a boil.","Simmer for 40 minutes until lentils are soft.","Add vermicelli noodles and cook for 5 more minutes.","Stir in fresh cilantro, parsley, and lemon juice before serving.","Serve hot with dates and chebakia during Ramadan."],
        "prepTimeMinutes":30,
        "cookTimeMinutes":50,
        "servings":6,
        "difficulty":"Medium",
        "userId" : 7,
        "cuisine":"Moroccan",
        "caloriesPerServing":380,
        "tags":["Soup","Moroccan","Ramadan"],
        "image":"https://cdn.dummyjson.com/recipe-images/51.webp",
        "rating":4.8,
        "reviewCount":74,
        "mealType":["Dinner","Lunch"]
    }
    recipe_holder = Recipe(**data)
    recipe_holder.assert_required_fields_exist()
    response = requests.post(f"{API_BASE_URL}/recipes/add", json = data , headers = headers)
    assert response.status_code == 200 , f"Something went wrong, response returned status code {response.status_code}"
    body = response.json()
    assert "id" in body , "Response haven't generated any identifier"
    recipe = Recipe(**body)
    recipe.assert_submitted_data_compatibility(data)
    return body["id"]

@pytest.mark.api
@pytest.mark.xfail(reason = "DummyJSON does not enforce server-side validation, expected 400 but API returns 200 regardless of payload")
def test_api_add_recipe_with_empty_payload(API_BASE_URL):
    response = requests.post(f"{API_BASE_URL}/recipes/add" , json = {})
    assert response.status_code == 400

@pytest.mark.api
@pytest.mark.xfail(reason="DummyJSON does not enforce server-side validation, expected 400 but API returns 200 regardless of payload")
def test_api_add_recipe_missing_fields(API_BASE_URL):
    data = {"name": "Harira Soup"}
    response = requests.post(f"{API_BASE_URL}/recipes/add", json=data)
    assert response.status_code == 400

@pytest.mark.api
@pytest.mark.smoke
def test_api_update_recipe(API_BASE_URL):
    payload = {
        "name" : "Moroccan 7arira with tomatoes"
    }
    response = requests.put(f"{API_BASE_URL}/recipes/7" , json = payload)
    assert response.status_code == 200 , f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    print(body)

@pytest.mark.api
@pytest.mark.smoke
def test_api_partial_update_recipe(API_BASE_URL):
    previous_recipe_name = requests.get(f"{API_BASE_URL}/recipes/1").json()["name"]
    payload = {
        "name" : "Italian Pizza - Margherita",
    }
    response = requests.put(f"{API_BASE_URL}/recipes/1", json=payload)
    assert response.status_code == 200, f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    assert previous_recipe_name != body["name"] , f"Something went wrong, expected the recipe name to be updated !" 

@pytest.mark.api
@pytest.mark.smoke
def test_api_complete_update_recipe(API_BASE_URL):
    payload = {
        "name": "Spicy Tomato Basil Bruschetta",
        "ingredients": ["Sourdough bread, sliced", "Tomatoes, diced", "Fresh basil, chopped", "Garlic cloves, minced", "Balsamic glaze", "Olive oil", "Red pepper flakes", "Salt and pepper to taste"],
        "instructions": [
            "Preheat the oven to 400°F (200°C).",
            "Place sourdough slices on a baking sheet and toast until golden brown.",
            "In a bowl, combine diced tomatoes, chopped fresh basil, minced garlic, red pepper flakes, and a drizzle of olive oil.",
            "Season with salt and pepper to taste.",
            "Top each toasted sourdough slice with the tomato-basil mixture.",
            "Drizzle with balsamic glaze and serve immediately."
        ],
        "prepTimeMinutes": 20,
        "cookTimeMinutes": 12,
        "servings": 8,
        "difficulty": "Medium",
        "cuisine": "Italian",
        "caloriesPerServing": 150,
        "tags": ["Bruschetta", "Italian", "Spicy"],
        "userId": 137,
        "image": "https://cdn.dummyjson.com/recipe-images/7.webp",
        "rating": 4.8,
        "reviewCount": 100,
        "mealType": ["Appetizer", "Snack"]
    }
    response = requests.put(f"{API_BASE_URL}/recipes/7", json=payload)
    assert response.status_code == 200 , f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    recipe = Recipe(**body)
    recipe.assert_payload_updated(payload)

@pytest.mark.api
@pytest.mark.smoke
def test_api_patch_recipe_attributes(API_BASE_URL):
    previous_details = requests.get(f"{API_BASE_URL}/recipes/7").json()
    patched_data = {
        "name" : "Random name for testing",
        "difficulty" : "Hard"
    }
    response = requests.patch(f"{API_BASE_URL}/recipes/7" , json=patched_data)
    assert response.status_code == 200 ,  f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    recipe = Recipe(**body)
    for field in body.keys():
        if field not in patched_data.keys():
            if field == "id":
                continue
            assert str(getattr(recipe, field)) == str(previous_details[field])
        else:
            assert str(getattr(recipe, field)) == str(patched_data[field])

@pytest.mark.api
@pytest.mark.xfail(reason="DummyJSON returns 200 for non-existing fields update, expected 400 since updating a non-existing field should be rejected")
def test_api_update_non_existing_recipe_fields(API_BASE_URL):
    payload = {
        "Chef" : "Enzo"
    }
    response = requests.put(f"{API_BASE_URL}/recipes/7" , json= payload)
    assert response.status_code == 200,  f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    assert "chef" not in body.keys() , "Non-existing fields must not be merged in the response"

