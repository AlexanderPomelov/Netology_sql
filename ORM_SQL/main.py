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

def get_shops(name):
    query = session.query(Book.title, Shop.name, Sale.price,Sale.date_sale,)\
    .select_from(Shop).join(Stock).join(Book).join(Publisher).join(Sale)
    if name.isdigit():
        query = query.filter(Publisher.id == name).all()
    else:
        query = query.filter(Publisher.name == name).all()
    for book, shop, price, date in query:
        print(f"{book: <40} | {shop: <10} | {price: <8} | {date.strftime('%d-%m-%Y')}")


if __name__ == '__main__':
    DSN = f'{driver_db}://{login_db}:{password_db}@{host_db}/{name_db}'
    engine = sqlalchemy.create_engine(DSN)
    Session = sessionmaker(bind=engine)
    session = Session()

    name = input('Введите имя или id: ')
    create_tables(engine) # создание таблиц
    drop_table(engine) # удаление таблиц
    data_add(path='tests_data.json') # добавление данных из json
    get_shops(name)  # выводит построчно факты покупки книг издателя

    session.commit()
    session.close()