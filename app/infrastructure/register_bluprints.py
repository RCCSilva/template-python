from flask import Flask


def register_blueprints(app: Flask):
    from app.features.orders.routes.order_routes import bp as order_bp

    app.register_blueprint(order_bp, url_prefix='/v1/orders')
