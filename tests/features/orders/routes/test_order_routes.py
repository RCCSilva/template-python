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

    assert len(response.json['items']) == 1
    assert response.json['items'][0]['name'] == p1.name
