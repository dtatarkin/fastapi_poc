from decimal import Decimal

from pydantic import BaseModel

from consts import State


class Order(BaseModel):
    quantity: Decimal
    price: Decimal
    state: State


class Invoice(BaseModel):
    amount_after_discount: Decimal
    total: Decimal
