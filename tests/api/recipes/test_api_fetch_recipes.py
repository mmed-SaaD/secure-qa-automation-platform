import pytest, requests
from src.api.recipe import Recipe

@pytest.mark.api
@pytest.mark.smoke
def test_api_get_all_recipes(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/recipes/")
    assert response.status_code == 200 , f"Something went wrong, request returned status code : {response.status_code}"
    body = response.json()
    assert "recipes" in body
    assert len(body["recipes"]) > 0 , "No recipes found !"
    for recipe in body["recipes"]:
        recipe = Recipe(**recipe)
        recipe.assert_required_fields_exist()

@pytest.mark.api
@pytest.mark.smoke
def test_api_get_recipe_by_id(API_BASE_URL, recipeID : int = 11):
    response = requests.get(f"{API_BASE_URL}/recipes/{recipeID}")
    assert response.status_code == 200 , f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    assert len(body) > 0 , "No reciped found !"
    recipe = Recipe(**body)
    recipe.assert_required_fields_exist()


