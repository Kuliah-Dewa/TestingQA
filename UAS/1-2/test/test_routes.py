import json
import requests
from .settings import DEFAULT_PRICE

def test_product_detail_api(client):
    id = 3
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')
    assert DEFAULT_PRICE * id


def test_product_api(client):
    response = client.get("/api/products")
    assert response.status_code == 200

#tugas 1 UAS
def test_create_cart_item():
    data = {
        "coupon_code": "dewa irtzadhany",
        "shipping_fee": 3,
        "cart_items": [
            {"product_id": 3, "qty": 3}
        ]
    }
    url = "http://127.0.0.1:5000/api/cart"
    response = requests.post(url, json=data)

    assert response.status_code == 200
    assert response.text == 'data created'
    
test_create_cart_item()