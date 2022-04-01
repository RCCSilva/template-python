from sqlalchemy import Column, Numeric, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from app import db


class OrderProduct(db.Model):
    __tablename__ = 'order_products'

    id = Column(BigInteger, primary_key=True)
    order_id = Column(BigInteger, ForeignKey('orders.id'))
    product_id = Column(BigInteger, ForeignKey('products.id'))
    price = Column(Numeric)

    order = relationship('Order')
    product = relationship('Product')
