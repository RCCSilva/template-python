from flask import Blueprint

bp = Blueprint('stock', __name__)

from app.features.orders.routes import order_routes  # noqa
