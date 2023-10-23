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
        ('+380662276711', 'This number was noticed in attempts to sell miracle water'),
        ('+380958775612', 'This number was asking me about 3 digits on the back of my card');
    
    INSERT INTO articles (title, desc, text) VALUES
        ('How not to fall for offers that sell miracle water', 'Short description', 'Here is the article'),
        ('Why you should not disclose your CVV number', 'Short description', 'Here is the article'),
        ('How not to fall for a scam in the crypto business', 'Short description', 'Here is the article'),
        ('How to buy cryptocurrency correctly', 'Short description', 'Here is the article'),
        ('Why you should not make your number public', 'Short description', 'Here is the article'),
        ('What to do if you get a call from a scammer', 'Short description', 'Here is the article');
''')

p_h1 = hashlib.sha256("hack1".encode()).hexdigest()
p_h2 = hashlib.sha256("hack2".encode()).hexdigest()

cursor.execute(f"INSERT INTO users (email, password) VALUES ('illia@gmail.com', '{p_h1}'), ('gorlach@gmail.com', '{p_h2}');")

conn.commit()
conn.close()
