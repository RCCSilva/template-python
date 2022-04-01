import logging

from app.features.orders.models.product import Product


class DiscountService:
    def __init__(self) -> None:
        self.__logger = logging.getLogger(__name__)

    def get_product_discount(self, product: Product) -> float:
        return product.base_price * 0.10
