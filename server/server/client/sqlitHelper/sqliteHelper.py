import sqlite3
from sqlite3 import Error

class dbhelper:
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn
    
    def insert_new_user(conn, db):
        sql = ''' INSERT INTO projects(name,begin_date,end_date)
                VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, db)
        conn.commit()
        return cur.lastrowid