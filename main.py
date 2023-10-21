import os
from flask import Flask, render_template, request
from flask_pymongo import PyMongo

from model import Model

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

m_user = os.environ.get('MONGO_USERNAME')
m_pass = os.environ.get('MONGO_PASSWORD')
m_db   = os.environ.get('MONGO_DB_NAME')
m_port = os.environ.get('MONGO_PORT')

app.config["MONGO_URI"] = f'mongodb://{m_user}:{m_pass}@localhost:{m_port}/{m_db}'
mongo = PyMongo(app)

model = Model(mongo)

@app.route('/', methods=['GET'])
def home() -> str:
    number = request.args.get('number')
    if number is None or number == '':
        return render_template('index.html',
                               message_visible='none',
                               comment_visible='none')
    else:
        comment = model.check_num(number)
        if comment is not None:
            message = f'Номер {number} є в базі даних шахраїв.'
            return render_template('index.html',
                                    message=message,
                                    comment=comment,
                                    style='red')
        else:
            message = f'Номеру {number} немає в базі даних шахраїв.'
            return render_template('index.html',
                                    message=message,
                                    comment_visible='none',
                                    style='green')
        
@app.route('/registration', methods=['POST'])
def registration() -> str:
    email    = request.form['email']
    password = request.form['password']

@app.route('/authorization.html', methods=['GET', 'POST'])
def authorization() -> str:
    if request.method == 'GET':
        return render_template('authorization.html')
    elif request.method == 'POST':
        pass


@app.route('/get_data')
def get_data():
    pass

if __name__ == '__main__':
    app.run()