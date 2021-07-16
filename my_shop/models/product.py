from sqlalchemy import Column, Integer, String
from my_shop.models.database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False, default="", server_default='')

    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, self.name)