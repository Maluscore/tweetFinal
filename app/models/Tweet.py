from . import db
from . import ReprMixin

import time


class Tweet(db.Model, ReprMixin):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    com_count = db.Column(db.Integer, default=0)
    # 这是一个外键
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = int(time.time())

    def json(self):
        self.id  # 加上这个就可以了
        _dict = self.__dict__.copy()
        d = {k: v for k, v in _dict.items() if k not in self.blacklist()}
        return d

    def blacklist(self):
        b = [
            '_sa_instance_state',
        ]
        return b

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, form):
        self.content = form.get('content', '')
        self.created_time = int(time.time())
        return True
