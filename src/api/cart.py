

class Cart:
    EXPECTED_CART_PRODUCT_KEYS = {
        "id":                 int,
        "title":              str,
        "price":              float,
        "quantity":           int,
        "total":              float,
        "discountPercentage": float,
        "discountedTotal":    float,
        "thumbnail":          str,
    }

    EXPECTED_CART_KEYS = {
        "id":               int,
        "products":         list,
        "total":            float,
        "discountedTotal":  float,
        "userId":           int,
        "totalProducts":    int,
        "totalQuantity":    int,
    }

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def from_dict(data: dict):
        return Recipe(**data)

    def assert_expected_cart_keys_exist_with_correct_types(self):
        for field, type in self.EXPECTED_CART_KEYS.items():
            assert isinstance(getattr(self, field), type) , \
            f"Expected {field} to have type {type} but got {type(getattr(self, field))}"