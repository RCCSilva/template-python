from app import db
from app.features.orders.models.order_product import OrderProduct
from app.features.orders.models.product import Product
from app.features.orders.routes import bp


@bp.route('/products', methods=['GET'])
def get_products():
    return {
        'items': [p.to_dict() for p in Product.query.all()],
    }


@bp.route('/order-products/<int:order_product_id>', methods=['DELETE'])
def delete_order_product(order_product_id: int):
    order_product = OrderProduct.query.get(order_product_id)

    db.session.delete(order_product)
    db.session.commit()

    return '', 200
