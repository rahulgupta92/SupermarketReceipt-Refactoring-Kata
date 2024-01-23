import pytest
from model_objects import Discount, Offer, Product, ProductUnit, SpecialOfferType


@pytest.mark.parametrize(
    "name,unit",
    [
        ("Apple", ProductUnit.KILO),
        ("Toothbrush", ProductUnit.EACH),
    ],
)
def test_product_creation(name, unit):
    product = Product(name, unit)
    assert product.name == name
    assert product.unit == unit


@pytest.mark.parametrize(
    "offer_type,product, argument",
    [
        (SpecialOfferType.THREE_FOR_TWO, Product("toothbrush", ProductUnit.EACH), None),
        (
            SpecialOfferType.TEN_PERCENT_DISCOUNT,
            Product("apple", ProductUnit.KILO),
            -10.0,
        ),
        (SpecialOfferType.TWO_FOR_AMOUNT, Product("toothpaste", ProductUnit.EACH), 40),
        (SpecialOfferType.FIVE_FOR_AMOUNT, Product("detergent", ProductUnit.KILO), 60),
    ],
)
def test_offer_creation(offer_type, product, argument):
    offer = Offer(offer_type, product, argument)
    assert offer.offer_type == offer_type
    assert offer.product == product
    assert offer.argument == argument


@pytest.mark.parametrize(
    "product,description,discount_amount",
    [
        (
            Product("apple", ProductUnit.KILO),
            "3 for 2",
            10.0,
        ),
        (
            Product("apple", ProductUnit.KILO),
            "10% off",
            10.0,
        ),
    ],
)
def test_discount_creation(product, description, discount_amount):
    discount = Discount(product, description, discount_amount)
    assert discount.product == product
    assert discount.description == description
    assert discount.discount_amount == discount_amount
