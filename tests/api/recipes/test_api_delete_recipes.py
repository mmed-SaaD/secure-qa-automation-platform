import requests, pytest

@pytest.mark.api
@pytest.mark.smoke
def test_api_delete_existing_recipe(API_BASE_URL, recipeID : int = 10):
    response = requests.delete(f"{API_BASE_URL}/recipes/{recipeID}")
    assert response.status_code == 200, f"Something went wrong, response returned status code {response.status_code}"

@pytest.mark.api
@pytest.mark.xfail(reason="Deleted recipes must not be retrievable, the target does not support this action")
def test_api_retreive_deleted_recipe(API_BASE_URL, recipeID: int = 10):
    response = requests.get(f"{API_BASE_URL}/recipes/{recipeID}")
    assert response.status_code == 404, f"Something went wrong, response returned status code {response.status_code}"

@pytest.mark.api
def test_api_delete_non_exisiting_recipe(API_BASE_URL, recipeID: int = 9999):
    response = requests.delete(f"{API_BASE_URL}/recipes/{recipeID}")
    assert response.status_code == 404, f"Something went wrong, response returned status code {response.status_code}"

@pytest.mark.api
@pytest.mark.xfail(reason="Attempting to delete already deleted recipes must raise an error !")
def test_api_repeatedly_deleting_recipe(API_BASE_URL, recipeID: int = 9999):
    #First attempt
    response = requests.delete(f"{API_BASE_URL}/recipes/{recipeID}")
    assert response.status_code == 200, f"Something went wrong, response returned status code {response.status_code}"
    #Second attempt
    response = requests.delete(f"{API_BASE_URL}/recipes/{recipeID}")
    assert response.status_code == 404, f"Something went wrong, response returned status code {response.status_code}"