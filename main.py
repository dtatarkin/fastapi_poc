from fastapi import FastAPI

from calc import get_invoice
from models import Order

app = FastAPI()


@app.post('/invoices')
def create_invoice(order: Order):
    return get_invoice(order)
