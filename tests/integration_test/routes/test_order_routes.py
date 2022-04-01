import json

import responses

from app.features.orders.models.order_product import OrderProduct
from tests.builders.order_builder import OrderBuilder
from tests.builders.order_product_builder import OrderProductBuilder
from tests.builders.product_builder import ProductBuilder


def test_get_products_given_products_return_products(client):
    # Arrange
    p1 = ProductBuilder() \
        .with_name('Teste!') \
        .build()

    # Act
    response = client.get('/v1/orders/products')

    # Assert
    assert response.status_code == 200

    assert len(response.json['items']) > 1
    assert response.json['items'][-1]['name'] == p1.name


def test_delete_order_product_given_existing_order_product_delete_product(client):
    # Arrange
    order_product = OrderProductBuilder() \
        .build()

    # Act
    response = client.delete(f'/v1/orders/order-products/{order_product.id}')

    # Assert
    assert response.status_code == 200

    order_product_db = OrderProduct.query.get(order_product.id)
    assert order_product_db is None


@responses.activate
def test_sync_order_given_existing_order(client):
    # Arrange
    order = OrderBuilder() \
        .build()

    responses.add(responses.POST, f'http://supertest', status=200)

    # Act
    response = client.post(f'/v1/orders/{order.id}/sync')

    # Assert
    assert response.status_code == 200
    body_json = json.loads(responses.calls[-1].request.body.decode('utf-8'))
    assert body_json['id'] == order.id
