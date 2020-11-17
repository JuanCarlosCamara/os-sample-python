from gatos.ninja.backend.database_connector import DatabaseConnector


class Model:
    def __init__(self):
        self.db = DatabaseConnector()

    def create_default(self):
        self.db.exec_statement('CREATE TABLE IF NOT EXISTS users(id INTEGER, name VARCHAR(25))')
        for i in range(100):
            self.db.exec_statement('INSERT INTO users (id, name) values ({0}, "{0}")'.format(i))


