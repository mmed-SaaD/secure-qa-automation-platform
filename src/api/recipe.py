from pydantic import HttpUrl
import requests

REQUIRED_FIELDS = {
        "name",
        "ingredients",
        "instructions",
        "prepTimeMinutes",
        "cookTimeMinutes",
        "servings",
        "difficulty",
        "cuisine",
        "caloriesPerServing",
        "tags",
        "userId",
        "image",
        "rating",
        "reviewCount",
        "mealType",
    }

class Recipe:    

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def from_dict(data: dict):
        return Recipe(**data)

    def assert_required_fields_exist(self):
        for field in REQUIRED_FIELDS:
            assert hasattr(self, field) , f"Missing attribute {field}"

    def assert_submitted_data_compatibility(self, data: dict):
        for field in data.keys():
            assert str(getattr(self, field)) == str(data[field]) , f"Expected value to be {data[field]}, got {getattr(self, field)} instead"

    def assert_payload_updated(self, updated_payload: dict):
        for field in updated_payload.keys():
            if field == "id":
                continue
            assert str(getattr(self, field)) == str(updated_payload[field]) ,\
            f"Expected {field} value to be {getattr(self, field)} got {updated_payload[field]} instead !"
    
    def update_recipe_attributes(self, payload: dict):
        for field in payload.keys():
            response = requests.put(f"{API_BASE_URL}/recipe/{self.id}", json = payload) 
            assert response.status_code == 200
            return response