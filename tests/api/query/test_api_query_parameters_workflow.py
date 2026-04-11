import pytest, requests
from src.api.user_informations.user import User

@pytest.mark.api
@pytest.mark.smoke
def test_api_user_search_query(API_BASE_URL, name : str ="john"):
    response = requests.get(f"{API_BASE_URL}/users/search?q={name}")
    assert response.status_code == 200, f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    assert len(body["users"]) > 0, f"No users found for query '{name}'"
    for user in body["users"]:
        u = User(**user)
        u.assert_expected_keys_exist_and_types_are_valid()
        user_fullName = f"{getattr(u, "firstName")} {getattr(u, "lastName")}".lower()
        assert name.lower() in user_fullName

@pytest.mark.api
@pytest.mark.smoke
def test_api_user_sort_query(API_BASE_URL):
    firstNames = []
    params = {
        "limit" : 100
    }
    response = requests.get(f"{API_BASE_URL}/users?sortBy=firstName&order=asc" , params = params)
    assert response.status_code == 200, f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    for user in body["users"]:
        firstNames.append(user['firstName'])
    assert firstNames == sorted(firstNames), "Users are not sorted by firstName ascending"

@pytest.mark.api
@pytest.mark.smoke
def test_api_user_filter_query(API_BASE_URL):
    response = requests.get(f"{API_BASE_URL}/users/filter?key=hair.color&value=Brown")
    assert response.status_code == 200, f"Something went wrong, request returned status code {response.status_code}"
    body = response.json()
    for user in body["users"]:
        assert user["hair"]["color"] == "Brown" , "Filter mecanism is not working as expected !"