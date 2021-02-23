from fastapi.testclient import TestClient

from calc import get_invoice
from consts import State
from main import app
from models import Order

client = TestClient(app)


def test_read_main():
    order = Order(quantity=1, price=100, state=State.AL)
    response = client.post('/invoices', data=order.json())
    assert response.status_code == 200
    assert response.json() == get_invoice(order).dict()
