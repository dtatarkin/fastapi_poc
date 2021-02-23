from decimal import Decimal

import pytest

from calc import calc_discount, calc_discount_percent, calc_tax, round_discount, round_tax, get_invoice
from consts import State, TAX
from models import Order, Invoice


@pytest.mark.parametrize('amount, expected', (
    [Decimal(0), Decimal(0)],
    [Decimal('1.23'), Decimal('1.23')],
    [Decimal('1.231'), Decimal('1.24')],
    [Decimal('1.239'), Decimal('1.24')],
    [Decimal('-1.239'), Decimal('-1.23')],
))
def test_round_discount(amount, expected):
    assert round_discount(amount) == expected


@pytest.mark.parametrize('amount, expected', (
    [Decimal(0), Decimal(0)],
    [Decimal(1000), Decimal(30)],
    [Decimal(1001), Decimal('30.03')],
    [Decimal(-1), Decimal(0)],
    [Decimal(-1000), Decimal(-30)],
))
def test_calc_discount(amount, expected):
    assert calc_discount(amount) == expected


@pytest.mark.parametrize('amount, expected', (
    [0, 0],
    [999, 0],
    [1000, 3],
    [4999, 3],
    [5000, 5],
    [50000, 15],
    [50001, 15],
    [100000, 15],
    [-1000, 3],
))
def test_calc_calc_discount_percent(amount, expected):
    assert calc_discount_percent(amount) == expected


@pytest.mark.parametrize('amount, expected', (
    [Decimal(0), Decimal(0)],
    [Decimal('1.23'), Decimal('1.23')],
    [Decimal('1.235'), Decimal('1.24')],
    [Decimal('1.225'), Decimal('1.22')],
))
def test_round_tax(amount, expected):
    assert round_tax(amount) == expected


@pytest.mark.parametrize('amount, state, expected', (
    [Decimal(0), State.UT, Decimal(0)],
    *([Decimal(100), state, TAX[state]] for state in State),
    *([Decimal(0), state, Decimal(0)] for state in State),
    *([Decimal(-100), state, TAX[state]] for state in State),
))
def test_calc_tax(amount, state, expected):
    assert calc_tax(amount, state) == expected


@pytest.mark.parametrize('order, expected', (
    [
        Order(quantity=1, price=100, state=State.AL),
        Invoice(amount_after_discount=Decimal('100.00'), total=Decimal('104.00')),
    ],
    [
        Order(quantity=2, price=1000, state=State.NV),
        Invoice(
            amount_after_discount=Decimal('1940'),  # (1000*2)−3%
            total=Decimal('2095.2'),  # 1940+8%
        ),
    ],
))
def test_get_invoice(order, expected):
    assert get_invoice(order) == expected
