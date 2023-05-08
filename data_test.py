from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db_library import Authors, Books, Readers, Registers

engine = create_engine("postgresql://dzhuma:admin@/library", echo=True)
session = Session(bind=engine)

engine.connect()
print(engine)
a1 = Authors(
    author_id=1,
    first_name="Александр",
    last_name="Пушкин"
)

b1 = Books(
    book_id=1,
    title="Капитанская дочка",
    genre="Классика",
    fk_author_id=1
)

r1 = Readers(
    reader_id=1,
    first_name="Василий",
    last_name="Пупкин",
    number_phone="89991234556",
    fk_books_id=1
)

reg1 = Registers(
    register_id=1,
    mode_move=1,
    fk_readers_id=1,
    fk_books_id=1
)
session.add_all([a1, b1, r1, reg1])
session.commit()
