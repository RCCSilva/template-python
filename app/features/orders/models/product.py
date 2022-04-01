from sqlalchemy import Column, String, Numeric, BigInteger

from app import db


class Product(db.Model):
    __tablename__ = 'products'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(64))
    base_price = Column(Numeric)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
