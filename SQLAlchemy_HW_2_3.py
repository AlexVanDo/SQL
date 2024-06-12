import sqlalchemy as sq
import json
from sqlalchemy.orm import sessionmaker
from SQLAlchemy_HW import create_tables, publisher, shop, book, stock, sale

login = input('Enter login: ')
password = input('Enter password: ')
db_name = input('Enter database name: ')
DSN = f'postgresql://{login}:{password}@localhost:5432/{db_name}'
engine = sq.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

with open('tests_data.json', 'r') as td:
    data = json.load(td)

for rec in data:
    model = {
        'publisher': publisher,
        'shop': shop,
        'book': book,
        'stock': stock,
        'sale': sale,
    }[rec.get('model')]
    session.add(model(id=rec.get('pk'), **rec.get('fields')))
    session.commit()

def books_sold(publisher_):
    req = session.query(shop, book, sale, stock, publisher
                    ).filter(shop.id == stock.id_shop
                             ).filter(book.id == stock.id_book
                                      ).filter(sale.id_stock == stock.id
                                               ).filter(book.id_publisher == publisher.id
                                                        ).filter(publisher.name == publisher_)
    for shop, book, sale, stock, publisher in req.all():
        print(book, shop, sale, sep=' | ')


publisher_id = session.query(publisher.id).filter(publisher.name.like(input('Enter publisher name: '))).scalar_subquery()
req = session.query(shop, book, sale, stock
                    ).filter(shop.id == stock.id_shop
                             ).filter(book.id == stock.id_book
                                      ).filter(sale.id_stock == stock.id
                                               ).filter(book.id_publisher == publisher_id)
for shop, book, sale, stock in req.all():
    print(book, shop, sale, sep=' | ')


session.close()