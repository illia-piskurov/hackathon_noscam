from flask_pymongo import PyMongo


class Model:
    def __init__(self, conn: PyMongo) -> None:
        self.conn = conn

    def insert_num(self, number: str, comment: str) -> None:
        pass
