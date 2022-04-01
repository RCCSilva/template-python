from app import db
from app.features.orders.models.product import Product


class ProductBuilder:
    def __init__(self):
        self.__model = Product(
            name='Test',
            base_price=20.0,
        )

    def with_name(self, name: str):
        self.__model.name = name
        return self

    def with_base_price(self, base_price: float):
        self.__model.base_price = base_price
        return self

    def build(self):
        db.session.add(self.__model)
        db.session.commit()

        return self.__model
