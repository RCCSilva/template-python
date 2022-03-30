from app.features.orders.models.product import Product
from app.features.orders.routes import bp


@bp.route('/products', methods=['GET'])
def get_products():
    return {
        'items': [p.to_dict() for p in Product.query.all()],
    }
