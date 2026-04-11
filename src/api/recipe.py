from pydantic import HttpUrl
import requests

REQUIRED_FIELDS = {
    "name":               str,
    "ingredients":        list,
    "instructions":       list,
    "prepTimeMinutes":    int,
    "cookTimeMinutes":    int,
    "servings":           int,
    "difficulty":         str,
    "cuisine":            str,
    "caloriesPerServing": int,
    "tags":               list,
    "userId":             int,
    "image":              str,
    "rating":             (float, int),
    "reviewCount":        int,
    "mealType":           list,
}

class Recipe:    

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def from_dict(data: dict):
        return Recipe(**data)

    def assert_fields_type_is_correct(self):
        for field, expected_type in REQUIRED_FIELDS.items():
            actual = getattr(self, field)
            assert isinstance(actual, expected_type), \
                f"Expected '{field}' to be {expected_type.__name__}, got {type(actual).__name__}"

    def assert_non_nullability(self):
        for field in REQUIRED_FIELDS.keys():
            assert getattr(self, field) is not None, f"{field} must not be None"

    def assert_string_not_empty(self):
        for field in REQUIRED_FIELDS.keys():
            if isinstance(field, str):
                assert getattr(self, field) != "" , f"{field} must not be empty !"
            assert len(getattr(self,"ingredients")) > 0,  "ingredients list must not be empty"
            assert len(getattr(self,"instructions")) > 0, "instructions list must not be empty"
            assert len(getattr(self,"tags")) > 0,         "tags list must not be empty"
            assert len(getattr(self, "mealType")) > 0,     "mealType list must not be empty"

    def assert_required_fields_exist(self):
        for field in REQUIRED_FIELDS.keys():
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