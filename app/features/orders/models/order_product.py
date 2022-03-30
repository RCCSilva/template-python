from sqlalchemy import Integer, Column

from app import db


class OrderProduct(db.Model):
    __tablename__ = 'order_products'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    product_id = Column(Integer)
    price = Column(Integer)
