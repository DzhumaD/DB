from data_test import session
from db_library import Authors, Books, Readers, Registers

for it in session.query(Readers):
    print(it.first_name, )
