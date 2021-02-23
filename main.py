from fastapi import FastAPI

from calc import get_invoice
from models import Invoice, Order

app = FastAPI()


@app.post('/invoices', response_model=Invoice)
def create_invoice(order: Order) -> Invoice:
    return get_invoice(order)
