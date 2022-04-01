from app import db
from app.features.orders.models.order_product import OrderProduct
from tests.builders.order_builder import OrderBuilder
from tests.builders.product_builder import ProductBuilder


class OrderProductBuilder:
    def __init__(self):
        self.__model = OrderProduct(
            price=10
        )

    def with_order_id(self, order_id: int):
        self.__model.order_id = order_id
        return self

    def with_product_id(self, product_id: int):
        self.__model.product_id = product_id
        return self

    def build(self):
        if self.__model.product_id is None:
            self.__model.product_id = ProductBuilder().build().id

        if self.__model.order_id is None:
            self.__model.order_id = OrderBuilder().build().id

        db.session.add(self.__model)
        db.session.commit()

        return self.__model
