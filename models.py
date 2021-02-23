from decimal import Decimal

from pydantic import BaseModel

from consts import State


class Order(BaseModel):
    """
    Model to represent customer's order
    """
    quantity: Decimal
    price: Decimal
    state: State


class Invoice(BaseModel):
    """
    Model to represent invoice
    :param amount_after_discount: subtotal amount including discount
    :param total: total amount to pay including discount and tax
    """
    amount_after_discount: Decimal
    total: Decimal
