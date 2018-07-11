from app import app
from flask import render_template


@app.route('/')  # '@' Означет что это вызов метода Дикоратора, он оборачивает результат функции НАД которой стоит.
def index():  # Определяем первую страницу
    name = 'Мишаня'
    return render_template('index.html', n=name)  # Возвращаем содержимое страницы и переменной.

@app.route('/seting')
def bootstrapSetings():
    return render_template('bootstrapSetings.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
