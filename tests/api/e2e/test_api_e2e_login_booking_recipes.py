import pytest, requests
from src.api.recipe import Recipe

@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.e2e
def test_api_e2e_login_recipes_booking(API_BASE_URL, api_login_token_verification, USERNAME_API, PASSWORD_API):
    login_token = api_login_token_verification
    assert login_token is not None , f"Missing login token"
    
    #create a recipe
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


    #get a recipe
    response = requests.get(f"{API_BASE_URL}/recipes/15")
    assert response.status_code == 200 , f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    assert len(body) > 0 , "No reciped found !"
    recipe = Recipe(**body)
    recipe.assert_required_fields_exist()

    #update a recipe (partial)
    previous_recipe_name = requests.patch(f"{API_BASE_URL}/recipes/1").json()["name"]
    payload = {
        "name" : "Italian Pizza - Margherita",
    }
    response = requests.put(f"{API_BASE_URL}/recipes/1", json=payload)
    assert response.status_code == 200, f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    assert previous_recipe_name != body["name"] , f"Something went wrong, expected the recipe name to be updated !" 

    #update a recipe (full)
    payload = {
        "name": "Moroccan Mint Tea",
        "ingredients": ["Green tea leaves", "Fresh mint leaves", "Sugar", "Boiling water", "Pine nuts for garnish"],
        "instructions": [
            "Rinse the teapot with boiling water to warm it up.",
            "Add green tea leaves and pour a small amount of boiling water. Swirl and discard to rinse the leaves.",
            "Add fresh mint leaves and sugar to the teapot.",
            "Pour boiling water over the mint and tea leaves.",
            "Let steep for 3-4 minutes.",
            "Pour tea from a height into glasses to create a froth.",
            "Garnish with pine nuts and a sprig of fresh mint before serving."
        ],
        "prepTimeMinutes": 5,
        "cookTimeMinutes": 10,
        "servings": 4,
        "difficulty": "Easy",
        "cuisine": "Moroccan",
        "caloriesPerServing": 60,
        "tags": ["Tea", "Moroccan", "Beverage"],
        "userId": 137,
        "image": "https://cdn.dummyjson.com/recipe-images/7.webp",
        "rating": 4.9,
        "reviewCount": 120,
        "mealType": ["Beverage", "Breakfast"]
    }
    response = requests.put(f"{API_BASE_URL}/recipes/7", json=payload)
    assert response.status_code == 200 , f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    recipe = Recipe(**body)
    recipe.assert_payload_updated(payload)

    #delete a recipe
    response = requests.delete(f"{API_BASE_URL}/recipes/15")
    assert response.status_code == 200, f"Something went wrong, response returned status code {response.status_code}"
