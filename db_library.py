from sqlalchemy import MetaData
from sqlalchemy import Table, Index, Integer, String, Column, Text, \
    DateTime, Boolean, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Authors(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    # books = relationship("Book")


class Books(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    genre = Column(String(100), nullable=False)
    fk_author_id = Column(Integer, ForeignKey('authors.author_id'), nullable=False)
    fk_reader_id = Column(Integer, ForeignKey('readers.reader_id'))

class Readers(Base):
    __tablename__ = 'readers'
    reader_id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    number_phone = Column(String(100), nullable=False)


class Registers(Base):
    __tablename__ = 'registers'
    register_id = Column(Integer, primary_key=True)
    mode_move = Column(Boolean, nullable=False) # True - взял, False - сдал.
    fk_reader_id = Column(Integer, ForeignKey('readers.reader_id'), nullable=False)
    fk_book_id = Column(Integer, ForeignKey('books.book_id'), nullable=False)
