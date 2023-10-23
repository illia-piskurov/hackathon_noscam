import hashlib
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
        ('+380958775612', 'Цей номер був питав мене про 3 цифри на карточці ззаду');
    
    INSERT INTO articles (title, desc, text) VALUES
        ('Як не попастися на продажу чудо-водічкі', 'Короткий опис', 'Тут стаття'),
        ('Чому не варто казати номер CVV', 'Короткий опис', 'Тут стаття'),
        ('Як не попастися на обман в криптобізнесі', 'Короткий опис', 'Тут стаття'),
        ('Як правильно купувати криптовалюту', 'Короткий опис', 'Тут стаття'),
        ('Чому не варто робити свій номер загальнодоступним', 'Короткий опис', 'Тут стаття'),
        ('Що робити якщо вам дзвонять шахраї', 'Короткий опис', 'Тут стаття');
''')

p_h1 = hashlib.sha256("hack1".encode()).hexdigest()
p_h2 = hashlib.sha256("hack2".encode()).hexdigest()

cursor.execute(f"INSERT INTO users (email, password) VALUES ('illia@gmail.com', '{p_h1}'), ('gorlach@gmail.com', '{p_h2}');")

conn.commit()
conn.close()
