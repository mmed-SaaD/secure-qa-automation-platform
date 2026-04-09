import requests, pytest
from core.utils.email_validation import email_validation
from src.api.user_informations.user import User

REQUIRED_FIELDS = ["id", "firstName", "lastName", "email"]

@pytest.mark.api
@pytest.mark.smoke
def test_get_all_users(API_BASE_URL):
    ids = []
    emails = []
    response = requests.get(f"{API_BASE_URL}/users")
    assert response.status_code == 200

    body = response.json()
    assert "users" in body
    assert len(body["users"]) > 0 , "Expected users list"
    for user in body["users"]:
        for field in REQUIRED_FIELDS:
            assert field in user, f"Missing required field ['{field}']"
        ids.append(user["id"])
        assert email_validation(user["email"]) == True , f"Email format is not valid : {user['email']}"
    assert len(ids) == len(set(ids)), "User ids are expected to be unique !"

@pytest.mark.api
@pytest.mark.smoke
def test_get_user_by_id(API_BASE_URL, userID: int = 10):
    response = requests.get(f"{API_BASE_URL}/users/{userID}")
    body = response.json()

    assert response.status_code == 200
    assert body["id"] == userID , f"Expected id to be {userID}, get {body['id']} instead"
    for field in REQUIRED_FIELDS:
        assert field in body

@pytest.mark.api
@pytest.mark.smoke
def test_user_related_schema(API_BASE_URL):
    endpoints = [
        requests.get(f"{API_BASE_URL}/users/19").json(),
        requests.get(f"{API_BASE_URL}/users").json()["users"][0]
    ]
    for user in endpoints:
        User(**user)
    
    