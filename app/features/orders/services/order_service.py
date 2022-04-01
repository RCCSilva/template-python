import logging
from app.features.orders.models.product import Product
from app.features.orders.models.order import Order
from app.features.orders.models.order_product import OrderProduct

from app.features.orders.services.discount_service import DiscountService


class OrderService:
    def __init__(self, discount_service: DiscountService = None):
        self.__discount_service = discount_service or DiscountService()
        self.__logger = logging.getLogger(__name__)

    def create(self, product: Product):
        discount = self.__discount_service.get_product_discount(product)

        order = Order()
        order_product = OrderProduct()

        order_product.order = order
        order_product.product = product
        order_product.price = product.base_price - discount

        return order, order_product
