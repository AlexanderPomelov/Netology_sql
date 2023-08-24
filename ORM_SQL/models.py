import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))

    def __str__(self):
        return (f'Publisher {self.id} | {self.name}')

class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer)
    book_id = sq.Column(sq.Integer, sq.ForeignKey('book.id'))
    shop_id = sq.Column(sq.Integer, sq.ForeignKey('shop.id'))

    def __str__(self):
        return f' Stock {self.id} | {self.count} | {self.book_id} | {self.shop_id}'

class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40))
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'))

    publisher = relationship(Publisher, backref='book')
    stock = relationship(Stock, backref='book')

    def __str__(self):
        return f'Book {self.id} | {self.title} | {self.publisher_id}'
class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))

    stock = relationship(Stock, backref='shop')

    def __str__(self):
        return f'Shop {self.id} | {self.name}'
class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.DateTime)
    count = sq.Column(sq.Integer)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('stock.id'))

    stock = relationship(Stock, backref='sale')

    def __str__(self):
        return f'Sale {self.id} | {self.price} | {self.date_sale} | {self.count} | {self.stock_id}'
def create_tables(engine):
    Base.metadata.create_all(engine)

def drop_table(engine):
    Base.metadata.drop_all(engine)