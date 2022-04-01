from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app import db


class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)

    products = relationship('OrderProduct')

    def to_dict(self):
        return {
            'id': self.id
        }
