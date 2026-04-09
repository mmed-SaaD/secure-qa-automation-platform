import requests, pytest
from core.logger.get_logger import get_logger
from src.api.product import Product

LOGGER = get_logger(__name__)


@pytest.mark.api
@pytest.mark.smoke
def test_api_get_all_carts(API_BASE_URL):
        response = requests.get(f"{API_BASE_URL}/carts")
        assert response.status_code == 200 , f"An error has occured, status_code : {response.status_code}"
        body = response.json()
        for cart in body["carts"]:
            assert "products" in cart , "The cart is empty !"
            assert len(cart["products"]) > 0
            for product in cart["products"]:
                product = Product.from_dict(product)
                product.assert_required_fields_exist()

@pytest.mark.api
@pytest.mark.smoke
def test_api_get_cart_by_id(API_BASE_URL, cartID = 11):
    response = requests.get(f"{API_BASE_URL}/carts/{cartID}")
    assert response.status_code == 200 , f"An error has occured, status_code : {response.status_code}"
    body = response.json()
    assert "products" in body , "cart does not contain any items !"

@pytest.mark.api
@pytest.mark.smoke
def test_api_get_cart_by_user(API_BASE_URL, userID = 20): #Try id 20 for cart with items
    response = requests.get(f"{API_BASE_URL}/carts/user/{userID}")
    assert response.status_code == 200,  f"An error has occured, status_code : {response.status_code}"
    body = response.json()
    assert "carts" in body
    if len(body["carts"]) > 0:
        for cart in body["carts"]:
            assert "products" in cart, "Cart does not contain any items"
            LOGGER.info("Cart recovered with items !")
    else:
        LOGGER.warning(f"The user with the id {userID} has no items in his cart !")

@pytest.mark.api
@pytest.mark.smoke
def test_api_cart_total_coherance(API_BASE_URL):
    total = requests.get(f"{API_BASE_URL}/carts").json()["total"]
    params = {
        "limit" : total
    }
    response = requests.get(f"{API_BASE_URL}/carts", params = params)
    assert response.status_code == 200 , f"An error has occured, status code is {response.status_code}"
    body = response.json()
    for cart in body["carts"]:
        cart_totals = []
        cart_discountedTotals = []
        products = 0
        quantity = 0
        for product in cart["products"]:
            products += 1
            quantity += product["quantity"]
            assert round(product["price"] * product["quantity"],2) == round(product["total"],2), \
            f"Something went wrong, expected total to be {product["price"] * product["quantity"]} got {product["total"]} instead"
            cart_totals.append(float(product["total"]))
            discount = ((product["total"] * product["discountPercentage"]) / 100)
            assert round((product["total"] - discount), 2) == round(product["discountedTotal"],2) , \
            f"Something went wrong, expected discounted total to be {product["total"] - discount} got {product["discountedTotal"]}"
            cart_discountedTotals.append(float(product["discountedTotal"]))
        assert round(float(cart["total"]),2) == round(sum(cart_totals), 2)
        assert round(cart["discountedTotal"],2) == round(sum(cart_discountedTotals), 2)
        assert cart["totalProducts"] == products
        assert cart["totalQuantity"] == quantity

    assert body["total"] == len(body["carts"])



