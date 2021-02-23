from decimal import Decimal
from enum import Enum


class State(str, Enum):
    UT = 'UT'
    NV = 'NV'
    TX = 'TX'
    AL = 'AL'
    CA = 'CA'


TAX = {
    State.UT: Decimal('6.85'),
    State.NV: Decimal('8'),
    State.TX: Decimal('6.25'),
    State.AL: Decimal('4'),
    State.CA: Decimal('8.25'),
}

DISCOUNT_PERCENT = (
    (1000, Decimal(3)),
    (5000, Decimal(5)),
    (7000, Decimal(7)),
    (10000, Decimal(10)),
    (50000, Decimal(15)),
)
