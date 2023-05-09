from data_test import session
from sqlalchemy import func
from db_library import Authors, Books, Readers, Registers
import sys

help = '''
usage: console.py [option] [arg]
Options and arguments:
table               : выводит таблицу пользователей с количеством книг на руках
like [id_reader]    : выводит любимый жанр пользователя с ID=id_reader    
'''

print(help)

def table_readers():
    "Выводит таблицу"
    print("Таблица: Книги у читателей")
    msg = session.query(Readers.first_name, func.count(Readers.reader_id)). \
        join(Books).group_by(Readers.first_name)
    for row in msg.all():
        print(row[0], "|", row[1])
# table_readers()

def popular_genre(id_reader=None):
    "Выводит любимый жанр пользователя"
    if id_reader:
        msg = session.query(func.max(Books.genre)). \
            join(Registers).join(Readers). \
            filter(Readers.reader_id == id_reader, Registers.mode_move == True)
        if msg.all()[0][0]:
            print(f"Любимый жанр пользователя ID={id_reader} {msg.all()[0][0]}")
        else:
            print("К сожалению, пользователь с таким ID не существует или не брал книги")
    else:
        print("Введите ID пользователя")
# popular_genre(2)

# print(sys.argv)


if len(sys.argv) > 1:
    if sys.argv[1] == "table":
        table_readers()
    elif sys.argv[1] == "like":
        if sys.argv[2]:
            popular_genre(sys.argv[2])
        else:
            print("Введите ID")
    else:
        print("нет такой команды")
else:
    print("Введите команду")