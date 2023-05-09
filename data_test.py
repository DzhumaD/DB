from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db_library import Authors, Books, Readers, Registers

engine = create_engine("postgresql://dzhuma:admin@/library", echo=False)
session = Session(bind=engine)
b = []
engine.connect()
# b.append(Authors(author_id=1, first_name="Александр", last_name="Пушкин"))
# b.append(Readers(reader_id=1, first_name="Василий", last_name="Пупкин", number_phone="89991234556",))
b.append(Books(book_id=1, title="Капитанская дочка", genre="Классика", fk_author_id=1, fk_reader_id=1))
b.append(Books(book_id=2, title="Евгений Онегин", genre="Классика", fk_author_id=1, fk_reader_id=1))
b.append(Books(book_id=3, title="Руслан и Людмила", genre="Классика", fk_author_id=1, fk_reader_id=1))
b.append(Books(book_id=4, title="Дубровский", genre="Классика", fk_author_id=1, fk_reader_id=1))

b.append(Registers(register_id=1, mode_move=1, fk_reader_id=1, fk_book_id=1))
b.append(Registers(register_id=2, mode_move=1, fk_reader_id=1, fk_book_id=2))
# session.query(Registers).delete() #удалить все записи
# session.add_all(b)
# session.commit()
