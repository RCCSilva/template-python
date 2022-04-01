from unittest.mock import MagicMock

from app.features.orders.services.order_service import OrderService
from tests.builders.product_builder import ProductBuilder


def test_create_order_given_product(app):
    # Arrange
    app.app_context().push()

    discount_service = MagicMock()
    discount_service.get_product_discount = MagicMock(return_value=20)

    order_service = OrderService(discount_service=discount_service)
    product = ProductBuilder() \
        .with_base_price(50) \
        .build()

    # Act
    _, order_product = order_service.create(product)

    # Assert
    assert order_product.price == 30
