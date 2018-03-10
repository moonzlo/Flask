from app import app
from flask import render_template


@app.route('/')  # '@' Означет что это вызов метода Дикоратора, он оборачивает результат функции НАД которой стоит.
def index():  # Определяем первую страницу
    name = 'Мишаня'
    return render_template('index.html', n=name)  # Возвращаем содержимое страницы и переменной.
