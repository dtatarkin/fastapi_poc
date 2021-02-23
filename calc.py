from decimal import ROUND_CEILING, ROUND_HALF_EVEN, Decimal, localcontext

from consts import DISCOUNT_PERCENT, TAX, State
from models import Invoice, Order


def calc_discount_percent(amount: Decimal) -> Decimal:
    discount_percent = Decimal(0)
    for threshold, percent in DISCOUNT_PERCENT:
        if abs(amount) < threshold:
            return discount_percent
        discount_percent = percent
    return discount_percent


def round_discount(amount: Decimal) -> Decimal:
    """
    Rounding discount amount to cents (in favor of the buyer)
    :param amount: raw discount in fractions of dollars
    :return: rounded discount
    """
    with localcontext() as context:
        context.rounding = ROUND_CEILING
        return amount.quantize(Decimal('0.00'))


def calc_discount(amount: Decimal) -> Decimal:
    return round_discount(amount * calc_discount_percent(amount) / 100)


def round_tax(amount: Decimal) -> Decimal:
    """
    Rounding discount amount to cents (using "banker's rounding")
    :param amount: raw value in fractions of dollars
    :return: rounded tax amount
    """
    with localcontext() as context:
        context.rounding = ROUND_HALF_EVEN
        return amount.quantize(Decimal('0.00'))


def calc_tax(amount: Decimal, state: State) -> Decimal:
    return round_tax(abs(amount) * TAX[state] / 100)


def get_invoice(order: Order) -> Invoice:
    """
    Generate Invoice object from provided Order
    :param order: Order object
    :return: Invoice object
    """
    subtotal = order.quantity * order.price
    discount = calc_discount(subtotal)
    amount_after_discount = subtotal - discount
    tax = calc_tax(amount_after_discount, order.state)
    total = amount_after_discount + tax
    return Invoice(amount_after_discount=amount_after_discount, total=total)
