from tests.builders.order_builder import OrderBuilder
from tests.builders.order_product_builder import OrderProductBuilder
from tests.builders.product_builder import ProductBuilder


def create_order_scenario():
    order = OrderBuilder() \
        .build()

    product1 = ProductBuilder() \
        .with_name('Banana') \
        .build()

    product2 = ProductBuilder() \
        .with_name('Chocolate') \
        .build()

    order_product1 = OrderProductBuilder() \
        .with_order_id(order.id) \
        .with_product_id(product1.id) \
        .build()

    order_product2 = OrderProductBuilder() \
        .with_order_id(order.id) \
        .with_product_id(product2.id) \
        .build()

    print(f'''
product: {product1.id} - {product1.name}''')
