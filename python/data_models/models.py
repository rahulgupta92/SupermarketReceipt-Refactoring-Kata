from enum import Enum

from pydantic import BaseModel, Field


class ProductUnit(str, Enum):
    EACH = "each"
    KILO = "kilo"


class Product(BaseModel):
    name: str
    unit: ProductUnit


class ProductQuantity(BaseModel):
    product: Product
    quantity: float = Field(ge=0)


class SpecialOfferType(str, Enum):
    THREE_FOR_TWO = "three_for_two"
    TEN_PERCENT_DISCOUNT = "ten_percent_discount"
    TWO_FOR_AMOUNT = "two_for_amount"
    FIVE_FOR_AMOUNT = "five_for_amount"


class Offer(BaseModel):
    offer_type: SpecialOfferType
    product: Product
    argument: float


class Discount(BaseModel):
    product: Product
    description: str
    discount_amount: float = Field(ge=0)
