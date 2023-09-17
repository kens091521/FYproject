import sqlite3

class SQLiteHelper:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_file)
        self.connection.execute("PRAGMA foreign_keys = 1")  # Enable foreign key support

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, parameters=None):
        cursor = self.connection.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def execute_update(self, query, parameters=None):
        cursor = self.connection.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        self.connection.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        return rows_affected

    def execute_script(self, script):
        cursor = self.connection.cursor()
        cursor.executescript(script)
        self.connection.commit()
        cursor.close()