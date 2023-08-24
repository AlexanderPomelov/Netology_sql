import sqlalchemy
import json
from pprint import pprint
from config import driver_db, login_db, password_db, host_db, name_db
from sqlalchemy.orm import sessionmaker
from models import create_tables, drop_table, Publisher, Book, Stock, Sale, Shop

def data_add(path):
    """Функция добавляющая данные в таблицу из json"""

    with open(path, encoding='utf-8') as file:
        json_data = json.load(file)
    for record in json_data:
        model = {
            'publisher': Publisher,
            'shop' : Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        result = session.add(model(id=record.get('pk'), **record.get('fields')))
    return result

if __name__ == '__main__':
    DSN = f'{driver_db}://{login_db}:{password_db}@{host_db}/{name_db}'
    engine = sqlalchemy.create_engine(DSN)
    name = input('Введите имя: ')
    # create_tables(engine) # создание таблиц
    # drop_table(engine) # удаление таблиц

    Session = sessionmaker(bind=engine)
    session = Session()

    query = (session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).\
             join(Publisher).join(Stock).join(Shop).join(Sale)).filter(Publisher.name.like(f'%{name}%')).all()
    pprint(query)

    session.commit()
    session.close()