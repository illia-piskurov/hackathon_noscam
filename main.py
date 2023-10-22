import os
from flask import Flask, render_template, request
from flask_pymongo import PyMongo

from model import Model

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

model = Model()

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
        
@app.route('/registration.html', methods=['GET', 'POST'])
def registration() -> str:
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        email    = request.form['email']
        password = request.form['password']
        model.insert_user(email, password)
        message = 'Ви вдало зареєструвалися на сайті'
        return render_template('index.html',
                               message=message,
                               comment_visible='none',
                               style='green')
    

@app.route('/authorization.html', methods=['GET', 'POST'])
def authorization() -> str:
    if request.method == 'GET':
        return render_template('authorization.html',
                               message_visible='none')
    elif request.method == 'POST':
        email    = request.form['email']
        password = request.form['password']
        if model.check_user(email, password):
            return render_template('index.html',
                                   message_visible='none',
                                   comment_visible='none')
        # Почати сесію
        else:
            message = 'Ви або не зареєстровані або помилилися в паролі 😔'
            return render_template('authorization.html',
                                   style='red',
                                   message=message)

@app.route('/articles.html', methods=['GET'])
def articles() -> str:
    articles = model.get_articles()
    if articles is not None:
        return render_template('articles.html', articles=articles)

@app.route('/article/<int:article_id>', methods=['GET'])
def view_article(article_id) -> str:
    article = model.get_article_by_id(article_id)
    return render_template('article.html', title=article[1], text=article[3])

@app.route('/add_number.html', methods=['GET'])
def add_number() -> str:
    number  = request.args.get('number')
    comment = request.args.get('comment')

    if number is not None and comment is not None:
        model.insert_num(number, comment)
        message = f'Номер {number} був успішно доданий в базу з коментарем "{comment}"'
        return render_template('add_number.html',
                               message=message,
                               style='green')
    else:
        return render_template('add_number.html',
                               message_visible='none')
    
@app.route('/add_article.html', methods=['GET'])
def add_article() -> str:
    title  = request.args.get('title')
    desc   = request.args.get('desc')
    text   = request.args.get('text')

    if title is not None and desc is not None and text is not None:
        model.insert_article(title, desc, text)
        message = f'Стаття "{title}" була успішно додана в базу даних'
        return render_template('add_article.html',
                               message=message,
                               style='green')
    else:
        return render_template('add_article.html',
                               message_visible='none')

if __name__ == '__main__':
    app.run()