import os
import sqlite3
from typing import Optional, List, Tuple

class Model:
    def __init__(self) -> None:
        self.db_name = os.environ.get('DB_NAME')
        conn    = sqlite3.connect(self.db_name)

        cursor = conn.cursor()

        cursor.executescript('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                desc TEXT NOT NULL,
                text TEXT NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS numbers (
                id INTEGER PRIMARY KEY,
                number TEXT NOT NULL,
                comment TEXT NOT NULL
            );
        ''')
        conn.commit()
        conn.close()


    def insert_num(self, number: str, comment: str) -> None:
        conn   = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO numbers (number, comment) VALUES ('{number}', '{comment}');")
        conn.commit()
        conn.close()

    def insert_user(self, email: str, password: str) -> None:
        conn   = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO users (email, password) VALUES ('{email}', '{password}');")
        conn.commit()
        conn.close()

    def insert_article(self, title: str, desc: str, text: str) -> None:
        conn   = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO articles (title, desc, text) VALUES ('{title}', '{desc}', '{text}');")
        conn.commit()
        conn.close()

    def check_num(self, number_to_find: str) -> Optional[str]:
        conn   = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM numbers;")
        numbers = cursor.fetchall()

        found = next((item[2] for item in numbers if item[1] == number_to_find), None)
        conn.close()
        return found

    def check_user(self, email: str, password: str) -> bool:
        conn   = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users;")
        users = cursor.fetchall()
        user_to_find = (email, password)

        result = any(user == user_to_find for user in users)
        conn.close()
        return result

    def get_articles(self) -> Optional[List[Tuple[str, str, str]]]:
        conn   = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM articles;")
        articles = cursor.fetchall()
        return articles

    def get_article_by_id(self, id: str) -> None:
        conn   = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM articles;")
        articles = cursor.fetchall()

        found = next((article for article in articles if article[0] == id), None)
        conn.close()
        return found