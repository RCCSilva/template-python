from app import db
from app.features.orders.models.product import Product


class ProductBuilder:
    def __init__(self):
        self.__model = Product()

    def with_name(self, name: str):
        self.__model.name = name
        return self

    def build(self):
        db.session.add(self.__model)
        db.session.commit()

        return self.__model
