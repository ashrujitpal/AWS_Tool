import sqlite3


class DatabaseConnection:

    def __init__(self, database):
        self.database = database

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_tb or exc_type or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
