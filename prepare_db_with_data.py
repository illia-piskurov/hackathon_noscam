import os
import sqlite3

db_name = os.environ.get('DB_NAME')
conn    = sqlite3.connect(db_name)

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

cursor.executescript('''
    INSERT INTO numbers (number, comment) VALUES
        ('+380662276711', 'Цей номер був помічений в спробах продати чудо-водічку'),
        ('+380958775612', 'Цей номер був помічений в спробах продати курево');
    
    INSERT INTO users (email, password) VALUES
        ('illia@gmail.com', 'hack1'),
        ('gorlach@gmail.com', 'hack2');
    
    INSERT INTO articles (title, desc, text) VALUES
        ('Як не попастися на продажу чудо-водічкі', 'В цій статті бла бла', 'Тут стаття');
''')

conn.commit()
conn.close()
