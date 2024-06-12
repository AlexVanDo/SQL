import sqlalchemy as sq
import json
from sqlalchemy.orm import sessionmaker
from SQLAlchemy_HW import create_tables, Publisher, Shop, Book, Stock, Sale

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
        'Publisher': Publisher,
        'Shop': Shop,
        'Book': Book,
        'Stock': Stock,
        'Sale': Sale,
    }[rec.get('model')]
    session.add(model(id=rec.get('pk'), **rec.get('fields')))
    session.commit()


def get_shops(person): 
    req = session.query( 
        Book.title, Shop.shop_name, Sale.price, Sale.data_sale 
    ).select_from(Shop).\
        join(Stock).\
        join(Book).\
        join(Publisher).\
        join(Sale) 
    if person.isdigit(): 
        person_data = req.filter(person == Publisher.id).all() 
    else:
        person_data = req.filter(person == Publisher.name).all() 
    for shp, bk, slp, dsl in person_data: 
        print(f"{shp: <40} | {bk: <10} | {slp: <8} | {dsl.strftime('%d-%m-%Y')}") 


if __name__ == '__main__':
    person = input("Enter Publisher name or id: ") 
    get_shops(person)     
session.close()