from sqlalchemy import Column, Integer, String

from app import db


class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
