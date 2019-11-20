import sqlite3


class DataManager:

    def __init__(self, db_name, method):
        self.db_name = db_name
        self.method = method

    def __enter__(self):
        self.conn_man = sqlite3.connect(self.db_name)
        return self.conn_man

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn_man.close()

        if exc_val:
            raise


with DataManager('my_db_2.db', 'w') as db:
    rez = db.cursor()
