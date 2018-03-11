from app import db
from datetime import datetime
import re


def slugify(s):  # Функция поиска и исправлению url страниц.
    pattern = r'[^\w+]'  # Ищет исключения
    return re.sub(pattern, '-', s)  # Заменяет их на дефис


class Post(db.Model):  # Класс по созданию постов, в базу данных.
    # Создаем параметры колонок для хранение в базе данных.
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created_data = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):  # args это Список (одна звездёочка). kwargs именнованные словари.
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<post id: {}, title: {}>'.format(self.id, self.title)