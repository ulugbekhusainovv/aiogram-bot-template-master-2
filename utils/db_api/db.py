import psycopg2
from data import config

class DataBase(object):
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='tg_bot',
            user='postgres',
            password=config.password,
            host='localhost',
            port=5432
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tg_user(
                            id SERIAL PRIMARY KEY,
                            tg_id BIGINT UNIQUE NOT NULL,
                            first_name VARCHAR(255) NOT NULL,
                            last_name VARCHAR(255) NULL,
                            username VARCHAR(255) NULL,
                            reg_date TIMESTAMP DEFAULT NOW()
                            )
                            ''')
    def add_user(self, tg_id, username, first_name, last_name):
        print("add_user")
        print(username, first_name, last_name, tg_id)

        

        self.cursor.execute('''INSERT INTO tg_user(tg_id, username, first_name, last_name) 
                            VALUES (%s, %s, %s, %s) ON CONFLICT (tg_id) DO NOTHING''',
                            (tg_id, username, first_name, last_name))
        self.connection.commit()
    def user_exists(self,tg_id):
        self.cursor.execute(f'''SELECT tg_id FROM tg_user WHERE tg_id={tg_id}''')
        return bool(self.cursor.fetchall())
    

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS category(
                            id BIGSERIAL PRIMARY KEY,
                            category_name VARCHAR(255) NOT NULL,
                            reg_date DATE NOT NULL
                            )
                            ''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS book(
                            id BIGSERIAL PRIMARY KEY,
                            category_id BIGINT REFERENCES category(id) ON DELETE CASCADE,
                            book_name VARCHAR(255) NOT NULL,
                            book_file VARCHAR(255) NOT NULL,
                            reg_date DATE NOT NULL
                            )
                            ''')
        
# import sqlite3

# class DataBase(object):
#     def __init__(self):
#         self.connection = sqlite3.connect('tg_bot.db')
#         self.cursor = self.connection.cursor()
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS tg_user(
#                             id INTEGER PRIMARY KEY,
#                             tg_id INTEGER UNIQUE NOT NULL,
#                             first_name TEXT NOT NULL,
#                             last_name TEXT NULL,
#                             username TEXT NULL,
#                             reg_date TEXT DEFAULT CURRENT_TIMESTAMP
#                             )
#                             ''')

#     def add_user(self, tg_id, username, first_name, last_name):
#         print("add_user")
#         print(username, first_name, last_name, tg_id)
#         self.cursor.execute('''INSERT OR IGNORE INTO tg_user(tg_id, username, first_name, last_name) 
#                             VALUES (?, ?, ?, ?)''',
#                             (tg_id, username, first_name, last_name))
#         self.connection.commit()
