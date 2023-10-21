from typing import Optional
from flask_pymongo import PyMongo


class Model:
    def __init__(self, conn: PyMongo) -> None:
        self.conn = conn

    def insert_num(self, number: str, comment: str) -> None:
        pass

    def insert_user(self, number: str, comment: str) -> None:
        pass

    def insert_article(self, number: str, comment: str) -> None:
        pass

    def check_num(self, number: str) -> Optional[str]:
        if number == '+380662276711':
            return 'comment'
        else:
            return None

    def get_user(self, number: str, comment: str) -> None:
        pass

    def get_articles(self, number: str, comment: str) -> None:
        pass

    def get_article(self, number: str, comment: str) -> None:
        pass