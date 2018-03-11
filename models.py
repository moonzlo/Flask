from app import db
from datetime import datetime
import re


def slugify(s):  # Функция поиска и исправлению url страниц.
    pattern = r'[^\w+]'  # Ищет исключения
    return re.sub(pattern, '-', s)  # Заменяет их на дефис


post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')))





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

    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))



    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<post id: {}, title: {}>'.format(self.id, self.title)

  # Класс миграции
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tag id: {}, name: {}'.format(self.id, self.name)