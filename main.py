import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

from model import Model

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

m_user = os.environ.get('MONGO_USERNAME')
m_pass = os.environ.get('MONGO_PASSWORD')
m_db   = os.environ.get('MONGO_DB_NAME')

app.config["MONGO_URI"] = f'mongodb://{m_user}:{m_pass}@localhost:27017/{m_db}'
mongo = PyMongo(app)

model = Model(mongo)

@app.route('/')
def home() -> str:
    return render_template('index.html')

@app.route('/number/<number>')
def search(number) -> str:
    return render_template('search.html', number=number)

@app.route('/get_data')
def get_data():
    pass

if __name__ == '__main__':
    app.run()