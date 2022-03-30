from app import db
from app.features.orders.models.order import Order


class OrderBuilder:
    def __init__(self):
        self.__model = Order()

    def build(self):
        db.session.add(self.__model)
        db.session.commit()

        return self.__model
