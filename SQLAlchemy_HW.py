import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

login = input('Enter login: ')
password = input('Enter password: ')
db_name = input('Enter database name: ')
DSN = f'postgresql://{login}:{password}@localhost:5432/{db_name}'
engine = sq.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, nullable=False, primary_key=True)
    name = sq.Column(sq.String(length=60), nullable=False, unique=True)


class book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, nullable=False, primary_key=True)
    title = sq.Column(sq.String(length=60), nullable=False, unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

    def __str__(self):
        return f'{self.title}'

class shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, nullable=False, primary_key=True)
    shop_name = sq.Column(sq.String(length=60), nullable=False, unique=True)

    def __str__(self):
        return f'{self.shop_name}'

class stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, nullable=False, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

class sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, nullable=False, primary_key=True)
    price = sq.Column(sq.Numeric(5, 2), nullable=False)
    data_sale = sq.Column(sq.DATE, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    def __str__(self):
        return f'{self.price} | {self.data_sale}'

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

session.close()