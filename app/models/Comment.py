from . import db
from . import ReprMixin

import time


class Comment(db.Model, ReprMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.INTEGER, default=0)
    sender_name = db.Column(db.String())
    tweet_id = db.Column(db.Integer, db.ForeignKey('tweets.id'))

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = int(time.time())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()