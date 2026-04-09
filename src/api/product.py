import requests
from dataclasses import dataclass

class Product:
    REQUIRED_FIELDS = ["id", "title", "price"]
    EXPECTED_TYPES = {
        "id" : int,
        "title" : str,
        "price" : (int, float),
        "category" : str
    }

    EXPECTED_KEYS = {
            "id", "title", "description", "category", "price", 
            "discountPercentage", "rating", "stock", "tags", 
            "brand", "sku", "weight", "dimensions", "warrantyInformation", 
            "shippingInformation", "availabilityStatus", "reviews", 
            "returnPolicy", "minimumOrderQuantity", "meta", 
            "images", "thumbnail"
        }
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def from_dict(data: dict):
        return Product(**data)

    def assert_product_id(self, id: int):
        assert int(self.id) == id , f"There is an ID missmatch, expected {id} got {self.id}"

    def assert_required_fields_exist(self):
        for required_field in self.REQUIRED_FIELDS:
            assert hasattr(self, required_field), f"{required_field} is missing !"

    def assert_fields_type(self):
        for field, expected_type in self.EXPECTED_TYPES.items():
            assert isinstance(getattr(self, field), expected_type), \
            f"Expected [{field}] to be {expected_type} got {type(getattr(self, field))}"

    def assert_price_is_positive(self):
        assert self.price > 0 , f"Expected price to be positive, got {self.price}"

    def assert_title_is_not_empty(self):
        assert self.title, "Title is expected to be non-empty !"

    def assert_category_is_not_empty(self):
        assert self.category, "Category is expected to be non-empty !"

    def assert_shape_stability(self):
        actual_keys = set(vars(self).keys())

        missing_keys = self.EXPECTED_KEYS - actual_keys
        extra_keys = actual_keys - self.EXPECTED_KEYS

        assert not missing_keys, f"The following keys are missing {missing_keys}"
        assert not extra_keys, f"The following keys are extras {extra_keys}"
