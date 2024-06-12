import sqlalchemy as sq
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'Publisher'

    id = sq.Column(sq.Integer, nullable=False, primary_key=True)
    name = sq.Column(sq.String(length=60), nullable=False, unique=True)


class Book(Base):
    __tablename__ = 'Book'

    id = sq.Column(sq.Integer, nullable=False, primary_key=True)
    title = sq.Column(sq.String(length=60), nullable=False, unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('Publisher.id'), nullable=False)

    def __str__(self):
        return f'{self.title}'

class Shop(Base):
    __tablename__ = 'Shop'

    id = sq.Column(sq.Integer, nullable=False, primary_key=True)
    shop_name = sq.Column(sq.String(length=60), nullable=False, unique=True)

    def __str__(self):
        return f'{self.shop_name}'

class Stock(Base):
    __tablename__ = 'Stock'

    id = sq.Column(sq.Integer, nullable=False, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('Book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('Shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

class Sale(Base):
    __tablename__ = 'Sale'

    id = sq.Column(sq.Integer, nullable=False, primary_key=True)
    price = sq.Column(sq.Numeric(5, 2), nullable=False)
    data_sale = sq.Column(sq.DATE, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('Stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    def __str__(self):
        return f'{self.price} | {self.data_sale}'

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)