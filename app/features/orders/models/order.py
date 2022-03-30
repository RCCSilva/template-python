from sqlalchemy import Column, Integer

from app import db


class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
